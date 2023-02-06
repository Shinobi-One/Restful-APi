# pylint: disable=missing-module-docstring
from rest_framework import status
from rest_framework.viewsets import ModelViewSet ,GenericViewSet
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin,DestroyModelMixin

from .serializer import Books_serializer,collection_serializer,Review_Serializer,Cart_Serializer,CartItem_Serializer
from .models import Books,collection,Review,CartItem,Cart
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

class All_In_One(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class =Books_serializer
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ['collection']
    search_fields = ['description']
    ordering_fields =['collection']
    pagination_class = PageNumberPagination


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

class CartSet(CreateModelMixin,
                  RetrieveModelMixin,
                  DestroyModelMixin,
                  GenericViewSet):
    queryset=Cart.objects.all()
    serializer_class = Cart_Serializer
    def delete(self,request,pk):
        carts = get_object_or_404(Cart,pk=pk)
        carts.delete()
        return Response({"error" :'object cannot be deleted'},status=status.HTTP_405_METHOD_NOT_ALLOWE)

class CartItemSet(ModelViewSet):
    queryset=CartItem.objects.all()
    serializer_class = CartItem_Serializer
    filter_backends =[OrderingFilter]
    ordering_fields = ['quantity']

    def get_serializer_context(self):
        return {"cart_id" : self.kwargs['cart_pk']}    