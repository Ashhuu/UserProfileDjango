from django.urls import path
from . import views

urlpatterns = [
    path('', views.details, name="home"),
    path('test/', views.test, name="test"),
    path('del/<id>', views.delCard, name="deleteCard")
]
