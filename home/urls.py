from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="kiki-home"),
    path('about/', views.about, name="kiki-about"),
    path('contact/', views.contact, name="kiki-contact"),
]
