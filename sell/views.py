from django.shortcuts import render, redirect
from . models import *

#from django.http import HttpResponse
# Create your views here.

def sell_home(request):
    if request.method == "POST":
        product_name = request.POST.get("product_name")
        product_description = request.POST.get("product_description")
        product_ownership = request.POST.get("product_ownership")
        product_location = request.POST.get("product_location")
        product_image = request.FILES.get("product_image")
        contact_number = request.POST.get("contact_number")
        #email_address = request.POST.get("email_address")
        
        print(product_name)
        print(product_description)
        print(product_ownership)
        print(product_location)
        print(product_image)
        print(contact_number)
        
        Sell_product.objects.create( 

            product_name=product_name,
            product_description=product_description,
            product_ownership=product_ownership,
            product_location=product_location,
            product_image=product_image,
            contact_number=contact_number,

        )
        redirect('sell/home.html')

    return render(request, 'sell/sell_home.html')

