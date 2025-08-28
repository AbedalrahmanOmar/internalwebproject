from django.urls import path
from django.contrib import admin
from .views import SalesListView, top_two_sales, sales_view, insert_sale_view, barcode_lookup, sales_performance_view

urlpatterns = [
    path('sales/', SalesListView.as_view(), name='sales-list'),
    path('admin/', admin.site.urls),
    path('top-sales/', top_two_sales),
    path('sales-view/', sales_view, name='sales-view'),
    path("insert-sale/", insert_sale_view, name="insert_sale"),
    path("barcode/", barcode_lookup, name="barcode_lookup"), 
    path('sales-staff-performance/', sales_performance_view, name='sales_staff_performance'),   
]
    