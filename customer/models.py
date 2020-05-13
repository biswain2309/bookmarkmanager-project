# from django.contrib.auth import get_user_model
from django.db import models


class Bookmark(models.Model):
    bid = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    sourcename = models.CharField(max_length=100)

    def __str__(self):
        return self.bid


class Customer(models.Model):
    bookmark = models.ForeignKey(
        Bookmark, on_delete=models.SET_NULL, null=True
    )
    customerid = models.CharField(max_length=100)
    customername = models.CharField(max_length=100)
    customerlan = models.DecimalField(max_digits=9, decimal_places=6)
    customerlon = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.customerid
    
    def __str__(self):
        return self.customername