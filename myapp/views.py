from django.shortcuts import render
from django.http import HttpResponse
from .models import Prosuct


def index(request):
    items = Prosuct.objects.all()
    context = {
        'items': items
    }
    return render(request, "myapp/index.html", context)



def indexItem(request, item_id):
    item = Prosuct.objects.get(id=item_id)
    context = {
        'item': item
    }
    return render(request, "myapp/detail.html", context)
