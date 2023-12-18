from django.urls import path
from . import views

app_name = "myapp"

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:item_id>/', views.indexItem, name='detailItem'),
    path('additem/', views.addItem, name='addItem'),
    path('updateitem/<int:item_id>/', views.updateItem, name='updateItem'),
    path('deleteitem/<int:item_id>/', views.deleteItem, name='deleteItem'),
]
