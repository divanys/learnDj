from django.shortcuts import render, redirect
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


def updateItem(request, item_id):
    item = Prosuct.objects.get(id=item_id)

    if request.method == "POST":
        item.name = request.POST.get("name")
        item.price = request.POST.get("price")
        item.description = request.POST.get("description")
        item.image = request.FILES.get('upload', item.image)
        item.save()
        return redirect('/myapp/')
    context = {
        'item': item
    }
    return render(request, 'myapp/updateitem.html', context)


def deleteItem(request, item_id):
    item = Prosuct.objects.get(id=item_id)

    if request.method == "POST":
        item.delete()
        return redirect('/myapp/')
    context = {
        'item': item
    }
    return render(request, 'myapp/deleteitem.html', context)

