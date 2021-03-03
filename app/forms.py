from django.forms import ModelForm
from app.models import Sellers, Products, Categories, Marketplaces


class SellersForm(ModelForm):
    class Meta:
        model = Sellers
        fields = ['name', 'social_reason', 'cnpj', 'email', 'phone', 'address']


class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'description', 'value', 'categories']


class CategoriesForm(ModelForm):
    class Meta:
        model = Categories
        fields = ['name', 'description']


class MarketplacesForm(ModelForm):
    class Meta:
        model = Marketplaces
        fields = ['name', 'description', 'site', 'phone', 'email', 'technical_manager']

