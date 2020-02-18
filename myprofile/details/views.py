from django.shortcuts import render

# Create your views here.

def details(request):
    return render(request, 'details/details.html', {})

def test(request):
    return render(request, 'details/test.html', {})