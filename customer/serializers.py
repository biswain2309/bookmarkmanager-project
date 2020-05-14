from rest_framework import serializers
from .models import Customer
from .models import Bookmark


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ('bid', 'title', 'url', 'sourcename')

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('bookmark', 'customerid', 'customername', 'customerlan', 'customerlon', 'customerrad')
        


