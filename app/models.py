from django.db import models
from django.utils.text import slugify
# Create your models here.

class stuff1(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    price=models.DecimalField(decimal_places=2,max_digits=20)
    name = models.CharField(max_length=50)
    collector = models.ForeignKey('collection',null=True,on_delete=models.CASCADE,related_name='collector')


class collection(models.Model):
    id =models.IntegerField(primary_key=True)
    detail=models.CharField(max_length=255)

    def __str__(self):
        return f"{self.num}"