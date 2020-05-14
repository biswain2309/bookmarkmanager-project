from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter,SearchFilter
from drf_multiple_model.views import ObjectMultipleModelAPIView


from .serializers import CustomerSerializer
from .serializers import BookmarkSerializer
from .models import Customer
from .models import Bookmark

class CustomerViewset(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    

class BookmarkViewset(viewsets.ModelViewSet):
    serializer_class = BookmarkSerializer
    queryset = Bookmark.objects.all()

class BrowseViewset(viewsets.ModelViewSet):
    serializer_class = BookmarkSerializer
    queryset = Bookmark.objects.all()
    filter_backends = (DjangoFilterBackend,OrderingFilter,)
    filter_fields = ('customer__customerid', 'customer__customerlan', 'customer__customerlon','creationdate')
    OrderingFields = ('title')