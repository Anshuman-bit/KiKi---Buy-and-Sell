from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home/home.html')


def about(request):
    return render(request, 'home/about.html')

def contact(request):
    if request.method=="POST":
        contact_number = request.POST.get('contact-number')
        email_address = request.POST.get('email-address')
        print(contact_number)
        print(email_address)
        redirect('home/home.html')
    
    return render(request, 'home/contact.html')
