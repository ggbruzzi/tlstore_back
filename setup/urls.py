from django.contrib import admin
from django.urls import path, include
from tlstore_back.views import UsersViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Users', UsersViewset, basename='Users')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
