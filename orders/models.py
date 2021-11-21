from django.db import models

# Create your models here.
class Types(models.Model):
    pizza = models.CharField(verbose_name="Tipo de pizza", max_length=50)
    size = models.CharField(verbose_name="Tamaño", max_length=75)
    price = models.FloatField(verbose_name="Precio")

    def __str__(self):
        return self.pizza

class Topings(models.Model):
    topings = models.CharField(verbose_name="Tipo de pizza", max_length=50)
    price = models.FloatField(verbose_name="Precio")

    def __str__(self):
        return self.topings

class Subs(models.Model):
    subs = models.CharField(verbose_name="Tipo de Sub", max_length=50)
    size = models.CharField(verbose_name="Tamaño", max_length=75)
    price = models.FloatField(verbose_name="Precio")

    def __str__(self):
        return self.subs

class Pasta(models.Model):
    pasta = models.CharField(verbose_name="pasta", max_length=50)
    price = models.FloatField(verbose_name="Precio")

    def __str__(self):
        return self.pasta

class Salads(models.Model):
    salads = models.CharField(verbose_name="Tipo de ensalada", max_length=50)
    price = models.FloatField(verbose_name="Precio")

    def __str__(self):
        return self.salads

class Dinner(models.Model):
    dinner = models.CharField(verbose_name="Platillo", max_length=50)
    size = models.CharField(verbose_name="Tamaño", max_length=75)
    price = models.FloatField(verbose_name="Precio")

    def __str__(self):
        return self.dinner