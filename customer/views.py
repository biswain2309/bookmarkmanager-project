from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter,SearchFilter


from .serializers import CustomerSerializer
from .serializers import BookmarkSerializer
from .models import Customer
from .models import Bookmark

class CustomerViewset(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all().order_by('customerid')
    

class BookmarkViewset(viewsets.ModelViewSet):
    serializer_class = BookmarkSerializer
    queryset = Bookmark.objects.all()

class BrowseViewset(viewsets.ModelViewSet):
    serializer_class = BookmarkSerializer
    queryset = Bookmark.objects.all()
    filter_backends = (DjangoFilterBackend,OrderingFilter,)
    filter_fields = ('customer__customername', 'customer__customerlan', 'customer__customerlon', 'sourcename', 'title',)
    OrderingFields = ('title')
    
    

