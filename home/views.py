from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    return render(request, 'home/home.html')


def about(request):
    return render(request, 'home/about.html')


def contact(request):
    if request.method == "POST":
        contact_number = request.POST.get('contact-number')
        email_address = request.POST.get('email-address')
        print(contact_number)
        print(email_address)
        return redirect('home/home.html')

        Home.objects.create(
            contact_number=contact_number,
            email_address=email_address,
        )
    return render(request, 'home/contact.html')

def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.filter(username=username)
        if user.exists():
            messages.warning(request, "Username already taken.")
            return redirect('/register/')

        print(first_name, last_name, username, password)

        User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password
        )
        messages.info(request, 'Account created successfully !')

        return redirect('/buy/')
    # Encrypted password - empty(for now)

    return render(request, 'home/register.html')



def kiki_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid credentials')
            return redirect('/kiki_login/')
        
        user = authenticate(username=username, password=password)
        
        if user is None:
            messages.error(request, 'Invalid credentials')
            return redirect('/kiki_login/')
        
        else:
            login(request, user)
            messages.success(request, "You're successfully logged in!")
            return redirect('/buy/')

    return render(request, 'home/login.html')