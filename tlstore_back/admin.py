from django.contrib import admin
from tlstore_back.models import *

class AdressA(admin.ModelAdmin):
    list_display = ('id','national_number', 'street', 'number', 'neighborhood', 'city', 'state')
    list_display_links = ('id', 'national_number')
    search_fields = ('id',)
    list_per_page = 20

admin.site.register(Adress, AdressA)


class UsersA(admin.ModelAdmin):
    list_display = ('id','name', 'surname', 'email', 'password', 'addresID' )
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(Users, UsersA)

class CountriesA(admin.ModelAdmin):
    list_display = ('id','name' )
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(Countries, CountriesA)


class CategoriesA(admin.ModelAdmin):
    list_display = ('id','name' )
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(Categories, CategoriesA)


class TeamsA(admin.ModelAdmin):
    list_display = ('id','name', 'country', 'category' )
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(Teams, TeamsA)


class ProductsA(admin.ModelAdmin):
    list_display = ('id','description', 'season', 'club', 'img', 'isImportant' )
    list_display_links = ('id', 'description')
    search_fields = ('description',)
    list_per_page = 20

admin.site.register(Products, ProductsA)


class SellsA(admin.ModelAdmin):
    list_display = ('id','date', 'userID', 'productID' )
    list_display_links = ('id', 'date')
    search_fields = ('date',)
    list_per_page = 20

admin.site.register(Sells, SellsA)





