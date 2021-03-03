"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from app.views import home, sellers, products, categories, marketplaces, categoriesForm, marketplacesForm, productsForm,\
    sellersForm, createCategories, createMarketplace, createProducts, createSellers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('sellers/', sellers, name='sellers'),
    path('products/', products, name='products'),
    path('categories/', categories, name='categories'),
    path('marketplaces/', marketplaces, name='marketplaces'),
    path('categoriesForm/', categoriesForm, name='categoriesForm'),
    path('marketplacesForm/', marketplacesForm, name='marketplacesForm'),
    path('productsForm/', productsForm, name='productsForm'),
    path('sellersForm/', sellersForm, name='sellersForm'),
    path('createCategories/', createCategories, name='createCategories'),
    path('createMarketplace/', createMarketplace, name='createMarketplace'),
    path('createProducts/', createProducts, name='createProducts'),
    path('createSellers/', createSellers, name='createSellers'),
]
