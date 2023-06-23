from django.shortcuts import render
from sell.models import *
from home.models import Home
#from django.http import HttpResponse
# Create your views here.

def buy_home(request):
    queryset = Sell_product.objects.all()
    context = {'products' : queryset}
    return render(request, 'buy/buy_home.html', context)

def contact_seller(request, id):
    queryset = Sell_product.objects.get(id=id)
    #queryset2 = Home.objects.all() 
    context = {'product': queryset}
    return render(request, 'buy/contact_seller.html', context)
