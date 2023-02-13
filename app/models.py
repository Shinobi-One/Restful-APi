from django.db import models
from uuid import uuid4
from django.conf import settings
# Create your models here.

class Customer(models.Model):
    MEMBERSHIP_GOLD ='G'
    MEMBERSHIP_SILVER ='S'
    MEMBERSHIP_BRONZE = "B"

    MEMBERSHIP_CHOICES= [
    (MEMBERSHIP_GOLD ,'Gold'),
    (MEMBERSHIP_SILVER, 'Silver'),
    (MEMBERSHIP_BRONZE, 'Bronze')

    ]

    Membership = models.CharField(max_length=1,default=MEMBERSHIP_BRONZE,choices=MEMBERSHIP_CHOICES)
    user =models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


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
    Books_review = models.ForeignKey(
        Books, on_delete=models.CASCADE, related_name='reviews',null=True)
    description =models.TextField()




class Cart(models.Model):
    id = models.UUIDField(default=uuid4,primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey('Cart',on_delete=models.CASCADE,related_name='items',null=True)
    Books = models.ForeignKey('Books',on_delete=models.CASCADE,default=0)
    quantity = models.PositiveSmallIntegerField(null=True)
