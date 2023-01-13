from django.db import models
from django.core.validators import MinLengthValidator
import bcrypt


class Adress(models.Model):
    national_number = models.CharField(max_length=8, validators=[MinLengthValidator(8)])
    street = models.CharField(max_length=50)
    number = models.IntegerField()
    neighborhood = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])

    def str(self):
      return str(self.pk)


class Users(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    addresID = models.ForeignKey(Adress, on_delete=models.CASCADE)



class Countries(models.Model):
    name = models.CharField(max_length=30, unique=True,)

    def str(self):
        return self.name.upper()



class Categories(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def str(self):
        return self.name.upper()



class Teams(models.Model):
    name = models.CharField(max_length=30, unique=True)
    country = models.ForeignKey(Countries, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def str(self):
        return self.name.upper()


class Products(models.Model):
    description = models.TextField(max_length=200)
    season = models.CharField(max_length=40)
    club = models.ForeignKey(Teams, on_delete=models.CASCADE)
    img = models.CharField(max_length=50)
    isImportant = models.BooleanField()


class Sells(models.Model):
    date = models.DateField()
    userID = models.ForeignKey(Users, on_delete=models.CASCADE)
    productID = models.ForeignKey(Products, on_delete=models.CASCADE)