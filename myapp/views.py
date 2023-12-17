from django.shortcuts import render
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


def addItem(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        image = request.FILES['upload']
        item = Prosuct(name=name, price=price, description=description, image=image)
        item.save()
    return render(request, 'myapp/additem.html')
