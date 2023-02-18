# pylint: disable=abstract-method
from rest_framework import  serializers
from decimal import Decimal
from app.models import Books,collection,Review,CartItem,Cart,Customer,Order,OrderItem
from django.db import transaction

class collection_serializer(serializers.ModelSerializer):
    class Meta:
        model = collection
        fields = ['id','detail','books']


class Books_Serializer(serializers.ModelSerializer):
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
        fields ="__all__"



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

class AddCartItem_Serializer(serializers.ModelSerializer):
    Books_id =serializers.IntegerField()

    def validate_Books_id(self,value):
        if not Books.objects.filter(pk=value).exists():
            raise serializers.ValidationError()


    def save(self, **kwargs):
        cart_id = self.context['cart_id']
        Books_id = self.validated_data['Books_id']
        quantity = self.validated_data['quantity']

        try: 
            cart_item = CartItem.objects.get(cart_id=cart_id, Books_id=Books_id)
            cart_item.quantity += quantity
            cart_item.save()
            self.instance = cart_item
        except CartItem.DoesNotExist:
            self.instance = CartItem.objects.create(cart_id=cart_id, **self.validated_data)
        
        return self.instance

    class Meta:
        model = CartItem
        fields = ['id', 'Books_id', 'quantity']


class UpdateCartItem_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['quantity']

class CustomerSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Customer
        fields = '__all__'

class OrderItem_Serializer(serializers.ModelSerializer):
    Books = Books_Serializer()
    class Meta:
        model = OrderItem
        fields = '__all__'
        
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItem_Serializer(many=True)
    class Meta:
        model = Order
        fields = ['id','customer','payment_status','placed_at','items']
        
class CreateOrderSerializer(serializers.Serializer):
    cart_id = serializers.UUIDField()
    
    
    def save(self, **kwargs):
        with transaction.atomic():
            cart_id=  self.validated_data['cart_id']
            user_id=  self.context['user_id']
            
            (customer,created) = Customer.objects.get_or_create(user_id = user_id)
            order=Order.objects.create(customer=customer)
            
            cart_item = CartItem.objects.select_related('Books').filter(cart_id= cart_id)
            items = [
                OrderItem(
                    order =order,
                    Books =item.Books,
                    quantity=item.quantity
                    ) for item in cart_item
                ]
            Order.objects.bulk_create(items)
            
            Cart.objects.filter(pk=cart_id).delete()