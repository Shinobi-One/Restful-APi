# pylint: disable=abstract-method
from rest_framework import  serializers
from decimal import Decimal
from app.models import stuff1,collection

class collection_serializer(serializers.Serializer):
    id = serializers.IntegerField()
    detail = serializers.CharField(max_length=255)


class stuff_serializer(serializers.ModelSerializer):
    class Meta:
        model = stuff1
        fields = ['id','title','price','name','taxes','collector']
    # id = serializers.IntegerField()
    # SHOWcase = serializers.CharField(max_length=255,source='title')
    # price=serializers.DecimalField(decimal_places=2,max_digits=20)
    taxes = serializers.SerializerMethodField(method_name='get_tax')
    # collector =serializers.HyperlinkedRelatedField(
    #     queryset=collection.objects.all(),
    #     view_name="collector-path"

    #     )



    def get_tax(self,product: stuff1):
        return product.price* Decimal(1.5)