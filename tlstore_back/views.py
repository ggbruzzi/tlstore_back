from rest_framework import viewsets
from tlstore_back.models import *
from tlstore_back.serializer import UsersSerializer

class UsersViewset(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer