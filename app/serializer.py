# pylint: disable=abstract-method
from rest_framework import  serializers
from decimal import Decimal
from app.models import Books,collection,Review,CartItem,Cart

class collection_serializer(serializers.ModelSerializer):
    class Meta:
        model = collection
        fields = ['id','detail','books']


class Books_serializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'
    # id = serializers.IntegerField()
    # SHOWcase = serializers.CharField(max_length=255,source='title')
    # price=serializers.DecimalField(decimal_places=2,max_digits=20)
    taxes = serializers.SerializerMethodField(method_name='get_tax')
    # description =serializers.HyperlinkedRelatedField(
    #     queryset=Books.objects.all(),
    #     many=True,view_name="reviews-detail")
    def get_tax(self,product: Books):
        return product.price* Decimal(1.5)


class Review_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields =['name','rate','description']



class SimpleBookSerializer(serializers.ModelSerializer):
    class Meta :
        model = Books
        fields =['id','description']



class CartItem_Serializer(serializers.ModelSerializer):
    Books = SimpleBookSerializer()

    class Meta:
        model = CartItem
        fields = ['id', 'Books', 'quantity']


class Cart_Serializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    items = CartItem_Serializer(many=True,read_only=True)
    total_price = serializers.SerializerMethodField(method_name='get_total_price')
    class Meta:
        model = Cart
        fields = ['id', 'items','total_price']


    def get_total_price(self,cart):
        for item in cart.items.all():
            return sum([item.quantity*item.Books.price])

# class CartItem_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = CartItem
#         fields = ['id','quantity','Books']



# class Cart_Serializer(serializers.ModelSerializer):
#     id = serializers.UUIDField(read_only=True)
#     items = CartItem_Serializer(many=True,read_only=True)
#     class Meta:
#         model = Cart
#         fields = ['id','items']
