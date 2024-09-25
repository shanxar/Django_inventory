from django.db import models

# Create your models here.
class Inventory_model(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    barcode=models.CharField(unique=True,max_length=30)
    
    def __str__(self) :
        return self.name