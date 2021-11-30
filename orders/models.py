from django.db import models
from django.conf import settings
# Create your models here.
class Pizza(models.Model):
    pizza = models.CharField(verbose_name="Tipo de pizza", max_length=50)
    stilo = models.CharField(verbose_name="Estilo", max_length=50)
    size = models.CharField(verbose_name="Tamaño", max_length=75)
    price = models.FloatField(verbose_name="Precio")


    def __str__(self):
        
        return self.pizza

    class Meta:
        verbose_name="Pizza"
        verbose_name_plural="Pizzas"

class Topings(models.Model):
    topings = models.CharField(verbose_name="Tipo_topping", max_length=50)
    
    class Meta:
        verbose_name="Topping"
        verbose_name_plural="Toppings"

    def __str__(self):
        return self.topings

class Subs(models.Model):
    subs = models.CharField(verbose_name="Tipo de Sub", max_length=50)
    size = models.CharField(verbose_name="Tamañosub", max_length=75)
    price = models.FloatField(verbose_name="Preciosub")

    class Meta:
        verbose_name="Sub"
        verbose_name_plural="Subs"

    def __str__(self):
        return self.subs

class Pasta(models.Model):
    pasta = models.CharField(verbose_name="pasta", max_length=50)
    price = models.FloatField(verbose_name="Preciopasta")

    class Meta:
        verbose_name="Pasta"
        verbose_name_plural="Pastas"

    def __str__(self):
        return self.pasta

class Salads(models.Model):
    salads = models.CharField(verbose_name="Tipo de ensalada", max_length=50)
    price = models.FloatField(verbose_name="Preciosalad")

    class Meta:
        verbose_name="Ensalada"
        verbose_name_plural="Ensaladas"

    def __str__(self):
        return self.salads

class Dinner(models.Model):
    dinner = models.CharField(verbose_name="Platillo", max_length=50)
    size = models.CharField(verbose_name="Tamañodinner", max_length=75)
    price = models.FloatField(verbose_name="Preciodinner")

    class Meta:
        verbose_name="Plato"
        verbose_name_plural="Platos"

    def __str__(self):
        return self.dinner




# Detalles de las ordenes

class Ordenes(models.Model):
    status=((0,"cancelado"),(1,"pendiente"),(2,"realizado"))
    cliente=models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="cliente", on_delete=models.CASCADE,related_name="orders")
    fecha=models.DateTimeField(verbose_name="tiempo",auto_now_add=True)
    estado=models.IntegerField(choices=status, default=1)

    

class detallepasta(models.Model):
    orden=models.ForeignKey(Ordenes, related_name="pastas", on_delete=models.CASCADE)
    pasta=models.ForeignKey(Pasta, related_name="items", on_delete=models.CASCADE)
    cantidad=models.IntegerField()
    price=models.FloatField(verbose_name="precio")

class detallepizza(models.Model):
    orden=models.ForeignKey(Ordenes, related_name="pizza", on_delete=models.CASCADE)
    pizza=models.ForeignKey(Pizza, related_name="items", on_delete=models.CASCADE)
    cantidad=models.IntegerField()
    price=models.FloatField()
    toppings=models.ManyToManyField(Topings)