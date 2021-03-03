from django.db import models

# Create your models here.
class Sellers(models.Model):
   name = models.CharField(max_length=80)
   social_reason = models.CharField(max_length=100)
   cnpj = models.IntegerField()
   email = models.CharField(max_length=80)
   phone = models.IntegerField()
   address = models.CharField(max_length=120)

class Products(models.Model):
   name = models.CharField(max_length=80)
   description = models.CharField(max_length=150)
   value = models.IntegerField()
   categories = models.CharField(max_length=120)


class Categories(models.Model):
   name = models.CharField(max_length=80)
   description = models.CharField(max_length=150)


class Marketplaces(models.Model):
   name = models.CharField(max_length=80)
   description = models.CharField(max_length=150)
   site = models.CharField(max_length=100)
   phone = models.IntegerField()
   email = models.CharField(max_length=100)
   technical_manager = models.CharField(max_length=120)

