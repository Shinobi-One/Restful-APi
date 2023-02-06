from django.db import models
from uuid import uuid4
# Create your models here.

class Books(models.Model):

    title = models.CharField(max_length=255)
    price=models.DecimalField(decimal_places=2,max_digits=20)
    collection = models.ForeignKey('collection',null=True,
                                  on_delete=models.CASCADE,related_name='books')
    last_update = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)

class collection(models.Model):
    detail=models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id}"


class Review(models.Model):
    name = models.CharField(max_length=256)
    rate = models.IntegerField()
    Books = models.ForeignKey(
        Books, on_delete=models.CASCADE, related_name='reviews',null=True)
    description =models.TextField()




class Cart(models.Model):
    id = models.UUIDField(default=uuid4,primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey('Cart',on_delete=models.CASCADE,related_name='items')
    Books = models.ForeignKey('Books',on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.id}"    