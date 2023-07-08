from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="kiki-home"),
    path('about/', views.about, name="kiki-about"),
    path('contact/', views.contact, name="kiki-contact"),
    path('register/', views.register, name="kiki-register"),
    path('kiki_login/', views.kiki_login, name="kiki-login"),
]
