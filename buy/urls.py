from . import views
from django.urls import path

urlpatterns = [
    path('', views.buy_home, name="buy-home"),
    path('contact_seller/<id>/', views.contact_seller, name="contact-seller"), 
]
