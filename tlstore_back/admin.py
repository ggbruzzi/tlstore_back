from django.contrib import admin
from tlstore_back.models import *

class AdressA(admin.ModelAdmin):
    list_display = ('id','national_number', 'street', 'number', 'neighborhood', 'city', 'state')
    list_display_links = ('id', 'national_number')
    search_fields = ('national_number',)
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





