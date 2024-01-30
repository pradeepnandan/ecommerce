"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from . import views
from django.contrib import admin
from django.urls import path,include
app_name='cart_app'

urlpatterns = [
    #path('',views.index,name='index'),
    path('add/<int:product_id>/',views.add_cart,name="add_cart"),
    path('',views.cart_details,name="cart_details"),
    path('remove/<int:product_id>/',views.remove_cart,name='remove_cart'),

]