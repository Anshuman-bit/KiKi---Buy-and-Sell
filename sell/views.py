from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User


# from django.http import HttpResponse
# Create your views here.

def sell_home(request):
    if request.method == "POST":
        product_name = request.POST.get("product_name")
        product_description = request.POST.get("product_description")
        product_ownership = request.POST.get("product_ownership")
        product_location = request.POST.get("product_location")
        product_image = request.FILES.get("product_image")
        contact_number = request.POST.get("contact_number")
        # email_address = request.POST.get("email_address")

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


def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")

        print(first_name, last_name, username, password)

        User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password
        )

        return redirect('/register/')

    return render(request, 'sell/register.html')


def login(request):
    return HttpResponse("<h1>Login page</h1>")
