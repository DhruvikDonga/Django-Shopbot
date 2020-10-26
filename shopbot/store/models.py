from django.db import models

# Create your models here.
class Storeitems(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=250)
    item_price = models.IntegerField()
    item_qty = models.IntegerField()