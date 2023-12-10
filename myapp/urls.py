from django.contrib import admin
from django.urls import path
from . import views

app_name = "myapp"

urlpatterns = [
    path('', views.index),
    path('<int:item_id>/', views.indexItem, name='detailItem'),
]
