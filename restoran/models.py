from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.TextField(blank=True)
    type = models.TextField(blank=True)
    price = models.IntegerField()
    description = models.TextField(blank=True)
    #m_pic = models.ImageField(upload_to=)


class Users(models.Model):
    login = models.TextField(blank=True)
    password = models.TextField(blank=True)
    name = models.TextField(blank=True)
    #u_pic = models.ImageField(upload_to=)


class Basket(models.Model):
    user = models.ForeignKey('Users', on_delete=models.PROTECT)
    manu = models.ForeignKey('Menu', on_delete=models.PROTECT)
    count = models.IntegerField()
    sum_price = models.IntegerField()