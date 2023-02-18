# pylint: disable=missing-module-docstring
from rest_framework import status
from rest_framework.viewsets import ModelViewSet ,GenericViewSet
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.mixins import UpdateModelMixin , CreateModelMixin,RetrieveModelMixin
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from .serializer import OrderSerializer,CreateOrderSerializer, Books_Serializer,CustomerSerializer,collection_serializer,Review_Serializer,Cart_Serializer,CartItem_Serializer,AddCartItem_Serializer,UpdateCartItem_Serializer
from .models import Books,collection,Review,CartItem,Cart,Customer,Order
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import CustomPermission,HistoryPermissions

class All_In_One(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class =Books_Serializer
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ['collection']
    search_fields = ['description']
    ordering_fields =['collection']
    pagination_class = PageNumberPagination
    permission_classes = [CustomPermission]


    def get_serializer_context(self):
        return {"request":self.request}

    def delete(self,request,pk):
        stuff = get_object_or_404(Books,pk=pk)
        stuff.delete()
        return Response({"error" :'object cannot be deleted'},
                        status=status.HTTP_405_METHOD_NOT_ALLOWED )



class Collection_Set(ModelViewSet):
    queryset = collection.objects.all()
    serializer_class = collection_serializer
    permission_classes = [CustomPermission]
    def get_serializer_context(self):
        return {"request":self.request}

    def delete(self,request,pk):
        collection = get_object_or_404(collection,pk=pk)
        collection.delete()
        return Response({"error" :'object cannot be deleted'},status=status.HTTP_405_METHOD_NOT_ALLOWED )        


class ReviewSet(ModelViewSet):
    queryset=Review.objects.all()
    serializer_class = Review_Serializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields =['rate']


    def get_serializer_context(self):
        return {"app_id" : self.kwargs['app_pk'] }

class CartSet(ModelViewSet):
    queryset=Cart.objects.all()
    serializer_class = Cart_Serializer

    def delete(self,request,pk):
        cart = get_object_or_404(Cart,pk=pk)
        cart.delete()
        return Response({"error" :'object cannot be deleted'},status=status.HTTP_405_METHOD_NOT_ALLOWED)

class CartItemSet(ModelViewSet):
    http_method_names = ['get','post','delete','patch']
    filter_backends =[OrderingFilter]
    ordering_fields = ['quantity']

    def get_queryset(self):
        return CartItem.objects.select_related('Books')

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCartItem_Serializer
        elif self.request.method == "PATCH":
            return UpdateCartItem_Serializer
        return CartItem_Serializer

    def get_serializer_context(self):
        return {"cart_id" : self.kwargs['cart_pk']}
class CustomerViewSets(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes= [IsAdminUser]

    def get_permissions(self,):
        if self.request.method == "GET":
            return [AllowAny()]
        return  [IsAuthenticated()]

    @action(detail=True, permission_classes=HistoryPermissions)
    def history(self,request,pk):
        return Response('ohayo')
    
    
    @action(detail=False, methods=['GET', 'PUT'],permission_classes=IsAdminUser)
    def me(self, request):
        (customer, created) = Customer.objects.get_or_create(
            user_id=request.user.id)
        if request.method == 'GET':
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        
        elif request.method == 'PUT':
            serializer = CustomerSerializer(customer, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
class OrderSet(ModelViewSet):
 
    permission_classes= [IsAuthenticated]
    
    
    def create(self, request, *args, **kwargs):
        serializer = CreateOrderSerializer(data=request.data,context= {'user_id' : self.request.user.id})
        serializer.is_valid(raise_exception=True)
        order= serializer.save()
        serializer= OrderSerializer(order)
        return Response(serializer.data)
    
    
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Order.objects.all()
        
        customer_id = Customer.objects.only('id').get(user_id = user.id)
        return Order.objects.filter(customer_id=customer_id)
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateOrderSerializer
        return OrderSerializer
        
        
