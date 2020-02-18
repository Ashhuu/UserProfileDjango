from django.db import models


class UserDetails(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40 )
    username = models.CharField(max_length=40, unique=True)
    password = models.CharField(max_length=40)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='static/images/',)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    skills = models.TextField()
    joined = models.DateTimeField(auto_now=True)
    empStatus = models.CharField(max_length=30)
    bio = models.TextField()


class CardDetails(models.Model):
    cardId = models.ForeignKey('UserDetails', on_delete=models.CASCADE)
    cardNumber = models.CharField(max_length=16)
    month = models.CharField(max_length=2)
    year = models.CharField(max_length=4)
    cvv = models.CharField(max_length=3)
    cardName = models.CharField(max_length=30)


class OrderDetails(models.Model):
    orderKey = models.ForeignKey('UserDetails',  on_delete=models.CASCADE)
    orderId = models.CharField(max_length=12, unique=True)
    trackingID = models.CharField(max_length=40)
    item = models.CharField(max_length=50)
    orderDate = models.DateTimeField()
