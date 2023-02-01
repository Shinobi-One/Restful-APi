# pylint: disable=abstract-method
from rest_framework import  serializers
from decimal import Decimal
from app.models import Books,collection,Review

class collection_serializer(serializers.ModelSerializer):
    class Meta:
        model = collection
        fields = ['detail']


class stuff_serializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['id','title','price','name','taxes','collector']
    # id = serializers.IntegerField()
    # SHOWcase = serializers.CharField(max_length=255,source='title')
    # price=serializers.DecimalField(decimal_places=2,max_digits=20)
    taxes = serializers.SerializerMethodField(method_name='get_tax')
    # description =serializers.StringRelatedField(read_only=True)



    def get_tax(self,product: Books):
        return product.price* Decimal(1.5)


class Review_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['title' , 'name' , 'rate' , 'description']