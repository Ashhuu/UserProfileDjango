from django.shortcuts import render
from . import models
from datetime import datetime
# Create your views here.

def details(request):
    details = models.UserDetails.objects.all()
    #addOrder()
    data = details[0]
    orderList = []
    if models.OrderDetails.objects.filter(orderKey=data).exists():
        orders = models.OrderDetails.objects.filter(orderKey=data).values()
        for i in orders:
            dicItem = {'item': i['item'], 'orderID': i['orderId'], 'trackingID': i['trackingID']}
            orderList.append(dicItem)
    else:
        orderList = None
    return render(request, 'details/details.html', {'data': data, 'order': orderList})


def addOrder():
    b = models.UserDetails.objects.get(username='ashhuu27')
    temp = 2
    orderID = [10101]
    temp = temp + orderID[-1]
    orderID.append(temp)
    order = models.OrderDetails.objects.create(orderKey=b, orderId = temp, orderDate = datetime.now(), item="Product2", trackingID = "778466")
    order.save()

def test(request):
    return render(request, 'details/test.html', {})