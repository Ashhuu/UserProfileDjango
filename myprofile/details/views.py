from django.shortcuts import render, redirect
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
    upload = forms.UploadImg()
    if models.OrderDetails.objects.filter(orderKey=data).exists():
        orders = models.OrderDetails.objects.filter(orderKey=data).values()
        for i in orders:
            dicItem = {'item': i['item'], 'orderID': i['orderId'], 'trackingID': i['trackingID']}
            orderList.append(dicItem)
    else:
        orderList = None
    if models.CardDetails.objects.filter(cardId=data).exists():
        card = models.CardDetails.objects.get(cardId=data)
    else:
        card = None
    if request.method == 'POST':
        form = forms.CardForm(request.POST)
        upload = forms.UploadImg(request.POST)
        if form.is_valid():
            cardDetails = form.cleaned_data
            card = models.CardDetails.objects.create(cardId=user,
                                                     cardNumber=cardDetails['cardNumber'],
                                                     month=cardDetails['month'],
                                                     year=cardDetails['year'],
                                                     cvv=cardDetails['cvv'],
                                                     cardName=cardDetails['name'])
            card.save()

    return render(request, 'details/details.html', {'data': data, 'order': orderList, 'form': form, 'card': card, 'form2': upload})


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


def delCard(request, id):
    if models.CardDetails.objects.filter(cardNumber=id).exists():
        models.CardDetails.objects.get(cardNumber=id).delete()
        return redirect('home')
    else:
        return redirect('home')