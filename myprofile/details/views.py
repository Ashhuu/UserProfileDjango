from django.shortcuts import render
from . import models
from . import forms
from datetime import datetime
# Create your views here.

def details(request):
    details = models.UserDetails.objects.all()
    user = models.UserDetails.objects.get(username='ashhuu27')
    #addOrder()
    data = details[0]
    orderList = []
    form = forms.CardForm()
    if models.OrderDetails.objects.filter(orderKey=data).exists():
        orders = models.OrderDetails.objects.filter(orderKey=data).values()
        for i in orders:
            dicItem = {'item': i['item'], 'orderID': i['orderId'], 'trackingID': i['trackingID']}
            orderList.append(dicItem)
    else:
        orderList = None
    if models.CardDetails.objects.filter(cardId=data).exists():
        #card = models.CardDetails.objects.filter(cardId=data).values()
        card = models.CardDetails.objects.get(cardId=data)
    else:
        card = None
    if request.method == 'POST':
        form = forms.CardForm(request.POST)
        if form.is_valid():
            cardDetails = form.cleaned_data
            card = models.CardDetails.objects.create(cardId=user,
                                                     cardNumber=cardDetails['cardNumber'],
                                                     month=cardDetails['month'],
                                                     year=cardDetails['year'],
                                                     cvv=cardDetails['cvv'],
                                                     cardName=cardDetails['name'])
            card.save()
    return render(request, 'details/details.html', {'data': data, 'order': orderList, 'form': form, 'card':card})


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