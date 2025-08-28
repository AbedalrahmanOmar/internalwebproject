from django.db import connection

def get_sales_sp(): #View Sales SP
    with connection.cursor() as cursor: #connection to the database by connection and cursor is used to execute SQL commands
        cursor.execute("EXEC dbo.Get_Sales")
        columns = [col[0] for col in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return results

def get_barcode(storeno, sku, size, colorcode): #Generate Barcode for Defect items
    with connection.cursor() as cursor:
        cursor.execute("""
            EXEC dbo.Get_Barcode_BY_SKU_SIZE_COLORCODE 
                @StoreNo=%s, 
                @SKU=%s, 
                @SIZE=%s, 
                @COLORCODE=%s
        """, [storeno, sku, size, colorcode])
        
        row = cursor.fetchone()
        return row[0] if row else None

def insert_sale(customer_name, product, quantity, sale_date, message=None):
    with connection.cursor() as cursor:
        cursor.execute("""
            EXEC dbo.Insert_Sale
                @CustomerName=%s,
                @Product=%s,
                @Quantity=%s,
                @SaleDate=%s,
                @Message=%s
        """, [customer_name, product, quantity, sale_date, message])

def get_sales_staff_performance():
    with connection.cursor() as cursor:
        # Execute the stored procedure
        cursor.execute("EXEC [dbo].[Get_Sales_Staff_Performance_Stores]")

        # Fetch results
        columns = [col[0] for col in cursor.description]  # get column names
        results = [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
    return results
from django.http import JsonResponse
