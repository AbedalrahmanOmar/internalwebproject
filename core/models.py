from django.db import models

class Sales(models.Model):
    saleid = models.AutoField(db_column='SaleID', primary_key=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=50, db_collation='Latin1_General_100_CS_AS', blank=True, null=True)  # Field name made lowercase.
    product = models.CharField(db_column='Product', max_length=50, db_collation='Latin1_General_100_CS_AS', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    saledate = models.DateField(db_column='SaleDate', blank=True, null=True)  # Field name made lowercase.
    message = models.CharField(db_column='Message', max_length=255, db_collation='Latin1_General_100_CS_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sales'
