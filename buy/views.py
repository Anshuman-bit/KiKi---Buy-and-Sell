from django.shortcuts import render
from sell.models import *
from sell.views import sell_home
#from django.http import HttpResponse
# Create your views here.

def buy_home(request):
    queryset = Sell_product.objects.all()
    context = {'products' : queryset}
    return render(request, 'buy/buy_home.html', context)

def contact_seller(request, id):
    queryset = Sell_product.objects.get(id=id)
    context = {'product': queryset}
    return render(request, 'buy/contact_seller.html', context)

