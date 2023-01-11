from django.db import models
from django.core.validators import MinLengthValidator


class Adress(models.Model):
    national_number = models.CharField(max_length=8, validators=[MinLengthValidator(8)])
    # ver se funcionou
    street = models.CharField(max_length=50)
    number = models.IntegerField()
    neighborhood = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    # ver se funcionou


class Users(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    # addresID =
    


class Countries(models.Model):
    name = models.CharField(max_length=30)
    # revisar


class Categories(models.Model):
    name = models.CharField(max_length=30)
    # revisar


class Teams(models.Model):
    name = models.CharField(max_length=30)
    # revisar
    # country = 
    # category = 

    

class Products(models.Model):
    description = models.TextField(max_length=200)
    season = models.CharField(max_length=40)
    # club = 
    # img =
    isImportant = models.BooleanField()


class Sells(models.Model):
    date = models.DateField()
    # userID = 
    # productID = 


