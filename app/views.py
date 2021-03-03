from django.shortcuts import render, redirect
from app.forms import SellersForm, ProductsForm, CategoriesForm, MarketplacesForm
from app.models import Categories, Products, Marketplaces, Sellers

# Create your views here.
def home(request):
    return render(request, 'index.html')

def sellers(request):
    data = {}
    data['db'] = Sellers.objects.all()
    return render(request, 'sellers.html', data)

def products(request):
    data = {}
    data['db'] = Products.objects.all()
    return render(request, 'products.html', data)

def categories(request):
    data = {}
    data['db'] = Categories.objects.all()
    return render(request, 'categories.html', data)

def marketplaces(request):
    data = {}
    data['db'] = Marketplaces.objects.all()
    return render(request, 'marketplaces.html', data)

def categoriesForm(request):
    data = {}
    data['formCategories'] = CategoriesForm()
    return render(request, 'categoriesForm.html', data)

def marketplacesForm(request):
    data = {}
    data['formMarketPlaces'] = MarketplacesForm()
    return render(request, 'marketplacesForm.html', data)

def productsForm(request):
    data = {}
    data['formProducts'] = ProductsForm()
    return render(request, 'productsForm.html', data)

def sellersForm(request):
    data = {}
    data['formSellers'] = SellersForm()
    return render(request, 'sellersForm.html', data)

def createCategories(request):
    form = CategoriesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def createMarketplace(request):
    form = MarketplacesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def createProducts(request):
    form = ProductsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def createSellers(request):
    form = SellersForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

