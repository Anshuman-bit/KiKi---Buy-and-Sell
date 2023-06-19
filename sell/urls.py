from . import views
from django.urls import path

urlpatterns = [
    path('', views.sell_home, name="sell-home"),
]
