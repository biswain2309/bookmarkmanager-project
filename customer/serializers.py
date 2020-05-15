from rest_framework import serializers
from .models import Customer
from .models import Bookmark


class BookmarkSerializer(serializers.ModelSerializer):
    """Serializes a Bookmark object"""
    class Meta:
        model = Bookmark
        fields = ('bid', 'title', 'url', 'sourcename','creationdate')

class CustomerSerializer(serializers.ModelSerializer):
    """Serializes a Customer object"""
    class Meta:
        model = Customer
        fields = ('bookmark', 'customerid', 'customername', 'customerlan', 'customerlon', 'customerrad')
        


