from django.shortcuts import render
from rest_framework.generics import *
from rest_framework.views import APIView
from applications.account.serializers import ProductSerializer
from applications.product.models import Product


class TaskListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CreateView(CreateAPIView):
    serializer_class = ProductSerializer


class DetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UpdateView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class DeleteView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
