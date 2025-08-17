from django.db import models

class Sales(models.Model):
    saleid = models.AutoField(db_column='SaleID', primary_key=True)
    customername = models.CharField(db_column='CustomerName', max_length=50, db_collation='Latin1_General_100_CS_AS', blank=True, null=True)
    product = models.CharField(db_column='Product', max_length=50, db_collation='Latin1_General_100_CS_AS', blank=True, null=True)
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)
    saledate = models.DateField(db_column='SaleDate', blank=True, null=True)
    message = models.CharField(db_column='Message', max_length=200, db_collation='Latin1_General_100_CS_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sales'
