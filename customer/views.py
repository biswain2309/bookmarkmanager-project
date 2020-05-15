from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter,SearchFilter
from drf_multiple_model.views import ObjectMultipleModelAPIView
from rest_framework import generics


from .serializers import CustomerSerializer
from .serializers import BookmarkSerializer
from .models import Customer
from .models import Bookmark

class CustomerViewset(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    

class BookmarkViewSet(viewsets.ModelViewSet):
    serializer_class = BookmarkSerializer
    queryset = Bookmark.objects.all()

class BrowseViewSet(viewsets.ModelViewSet):
    serializer_class = BookmarkSerializer
    queryset = Bookmark.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = ('customer__customerid', 'customer__customerlan', 'customer__customerlon','title')
    search_fields = ('customer__customerid', 'customer__customerlan', 'customer__customerlon','title')
    OrderingFields = ('bid', 'title', 'url', 'sourcename','creationdate')