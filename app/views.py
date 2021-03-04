from django.shortcuts import render, redirect
from app.forms import SellersForm, ProductsForm, CategoriesForm, MarketplacesForm
from app.models import Categories, Products, Marketplaces, Sellers
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    return render(request, 'index.html')

def sellers(request):
    data = {}
    data['db'] = Sellers.objects.all()
    return render(request, 'sellers.html', data)

def products(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Products.objects.filter(name__icontains=search) or Products.objects.filter(description__icontains=search) \
                     or Products.objects.filter(value__icontains=search) or Products.objects.filter(categories__icontains=search)
    else:
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
        return redirect('categories')

def createMarketplaces(request):
    form = MarketplacesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('marketplaces')

def createProducts(request):
    form = ProductsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('products')

def createSellers(request):
    form = SellersForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('sellers')

def viewCategorie(request, pk):
    data = {}
    data['db'] = Categories.objects.get(pk=pk)
    return render(request, 'viewCategorie.html', data)

def viewMarketplace(request, pk):
    data = {}
    data['db'] = Marketplaces.objects.get(pk=pk)
    return render(request, 'viewMarketplace.html', data)

def viewSeller(request, pk):
    data = {}
    data['db'] = Sellers.objects.get(pk=pk)
    return render(request, 'viewSeller.html', data)

def viewProduct(request, pk):
    data = {}
    data['db'] = Products.objects.get(pk=pk)
    return render(request, 'viewProduct.html', data)

def editCategorie(request, pk):
    data = {}
    data['db'] = Categories.objects.get(pk=pk)
    data['formCategories'] = CategoriesForm(instance=data['db'])
    return render(request, 'categoriesForm.html', data)

def updateCategorie(request, pk):
    data = {}
    data['db'] = Categories.objects.get(pk=pk)
    form = CategoriesForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('categories')

def editMarketplace(request, pk):
    data = {}
    data['db'] = Marketplaces.objects.get(pk=pk)
    data['formMarketPlaces'] = MarketplacesForm(instance=data['db'])
    return render(request, 'marketplacesForm.html', data)

def updateMarketplace(request, pk):
    data = {}
    data['db'] = Marketplaces.objects.get(pk=pk)
    form = MarketplacesForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('marketplaces')

def editSeller(request, pk):
    data = {}
    data['db'] = Sellers.objects.get(pk=pk)
    data['formSellers'] = SellersForm(instance=data['db'])
    return render(request, 'sellersForm.html', data)

def updateSeller(request, pk):
    data = {}
    data['db'] = Sellers.objects.get(pk=pk)
    form = SellersForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('sellers')

def editProduct(request, pk):
    data = {}
    data['db'] = Products.objects.get(pk=pk)
    data['formProducts'] = ProductsForm(instance=data['db'])
    return render(request, 'productsForm.html', data)

def updateProduct(request, pk):
    data = {}
    data['db'] = Products.objects.get(pk=pk)
    form = ProductsForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('products')

def deleteCategorie(request, pk):
    db = Categories.objects.get(pk=pk)
    db.delete()
    return redirect('categories')

def deleteMarketplace(request, pk):
    db = Marketplaces.objects.get(pk=pk)
    db.delete()
    return redirect('marketplaces')

def deleteSeller(request, pk):
    db = Sellers.objects.get(pk=pk)
    db.delete()
    return redirect('sellers')

def deleteProduct(request, pk):
    db = Products.objects.get(pk=pk)
    db.delete()
    return redirect('products')




