from django.db import models

# Create your models here.

class Books(models.Model):

    title = models.CharField(max_length=255)
    price=models.DecimalField(decimal_places=2,max_digits=20)
    name = models.CharField(max_length=50)
    collector = models.ForeignKey('collection',null=True,on_delete=models.CASCADE,related_name='collector')
    description = models.ForeignKey('Review',null=True,on_delete=models.CASCADE,related_name="reviews")

class collection(models.Model):
    detail=models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id}"

class Review(models.Model):
    title= models.ForeignKey('Books',null=False,on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    rate = models.IntegerField()
    description = models.TextField()

