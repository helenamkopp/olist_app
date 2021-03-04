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
    sellersForm, createCategories, createMarketplaces, createProducts, createSellers, viewCategorie, viewMarketplace,\
    viewSeller, viewProduct, editCategorie, updateCategorie, editMarketplace, updateMarketplace, editSeller, updateSeller, \
    editProduct, updateProduct, deleteCategorie, deleteMarketplace, deleteSeller, deleteProduct

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
    path('createMarketplaces/', createMarketplaces, name='createMarketplaces'),
    path('createProducts/', createProducts, name='createProducts'),
    path('createSellers/', createSellers, name='createSellers'),
    path('viewCategorie/<int:pk>/', viewCategorie, name='viewCategorie'),
    path('viewMarketplace/<int:pk>/', viewMarketplace, name='viewMarketplace'),
    path('viewSeller/<int:pk>/', viewSeller, name='viewSeller'),
    path('viewProduct/<int:pk>/', viewProduct, name='viewProduct'),
    path('editCategorie/<int:pk>/', editCategorie, name='editCategorie'),
    path('updateCategorie/<int:pk>/', updateCategorie, name='updateCategorie'),
    path('editMarketplace/<int:pk>/', editMarketplace, name='editMarketplace'),
    path('updateMarketplace/<int:pk>/', updateMarketplace, name='updateMarketplace'),
    path('editSeller/<int:pk>/', editSeller, name='editSeller'),
    path('updateSeller/<int:pk>/', updateSeller, name='updateSeller'),
    path('editProduct/<int:pk>/', editProduct, name='editProduct'),
    path('updateProduct/<int:pk>/', updateProduct, name='updateProduct'),
    path('deleteCategorie/<int:pk>/', deleteCategorie, name='deleteCategorie'),
    path('deleteMarketplace/<int:pk>/', deleteMarketplace, name='deleteMarketplace'),
    path('deleteSeller/<int:pk>/', deleteSeller, name='deleteSeller'),
    path('deleteProduct/<int:pk>/', deleteProduct, name='deleteProduct'),


]
