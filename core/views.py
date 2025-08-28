from django.http import JsonResponse
from rest_framework import generics
from .models import Sales
from .serializers import SalesSerializer
from .services import get_sales_sp, get_barcode, insert_sale, get_barcode, get_sales_staff_performance
import json
from django.views.decorators.csrf import csrf_exempt



def sales_performance_view(request):
    data = get_sales_staff_performance()
    return JsonResponse(data, safe=False)

@csrf_exempt
def barcode_lookup(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST allowed"}, status=405)

    try:
        body = json.loads(request.body.decode("utf-8"))
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    #the keys you use in body.get() must exactly match the keys in the JSON you send.
    store_no = body.get("StoreNo")
    sku = body.get("SKU")
    size = body.get("SIZE")
    color = body.get("COLORCODE")

    if not all([store_no, sku, size, color]):
        return JsonResponse({"error": "Missing parameters"}, status=400)

    barcode = get_barcode(store_no, sku, size, color)
    return JsonResponse({"barcode": barcode})

@csrf_exempt
def insert_sale_view(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))

        customer_name = data.get("customer_name")
        product = data.get("product")
        quantity = data.get("quantity")
        sale_date = data.get("sale_date")
        message = data.get("message", "New sale recorded")

        insert_sale(customer_name, product, quantity, sale_date, message)

        return JsonResponse({"status": "success", "message": "Sale inserted successfully!"})
    
    return JsonResponse({"error": "POST request required"}, status=400)


# Stored procedure view
def sales_view(request):
    data = get_sales_sp()
    return JsonResponse(data, safe=False)

# ORM query view
def top_two_sales(request):
    rows = Sales.objects.order_by('saleid')[:2]
    return JsonResponse({'sales': list(rows.values())})

# DRF List view
class SalesListView(generics.ListAPIView):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
