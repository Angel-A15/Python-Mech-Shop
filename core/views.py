from django.shortcuts import render
from .models import Item
from django.views.generic import ListView, DetailView

# def item_list(request):
#     context = {
#         'items': Item.objects.all()
#     }
#     return render(request, "item_list.html", context)

def products(request):
    context ={
        'items': Item.objects.all()
    }
    return render(request, "product.html", context)
    

def checkout(request):
    return render(request, "checkout.html", context)

class HomeView(ListView):
    model = Item
    template_name = "home.html"

class ItemDetailview(DetailView):
    model = Item
    template_name = "product.html"