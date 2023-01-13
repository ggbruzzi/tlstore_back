from rest_framework import viewsets, status
from tlstore_back.models import *
from tlstore_back.serializer import UsersSerializer, AdressSerializer
from rest_framework.response import Response
import bcrypt

class UsersViewSet(viewsets.ModelViewSet):
  queryset = Users.objects.all()
  serializer_class = UsersSerializer
  querysetAdress = Adress.objects.all()
  serializer_class_adress = AdressSerializer

  def create(self, request):
    AdressData = {
      "state": request.data.get('state'),
      "city": request.data.get('city'),
      "neighborhood": request.data.get('neighborhood'),
      "street": request.data.get('street'),
      "national_number": request.data.get('national_number'),
      "number": request.data.get('number')
    }
    serializer_adress = self.serializer_class_adress(data=AdressData)
    if serializer_adress.is_valid() and serializer_user.is_valid():
      serializer_adress.save()
    else:
      response = Response(serializer_adress.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
      return response

    senha = bcrypt.hashpw(request.data.get('password').encode(), bcrypt.gensalt(8))
    print(senha)
    UserData = {
      "name": request.data.get('name'),
      "surname": request.data.get('surname'),
      "email": request.data.get('email'),
      "password": str(senha),
      "addresID": str(serializer_adress.data['id'])
    }
    serializer_user = self.serializer_class(data=UserData)
    if serializer_user.is_valid():
      serializer_user.save()
      response = Response(serializer_user.data, status=status.HTTP_201_CREATED)
      id = str(serializer_user.data['id'])
      response['Location'] = request.build_absolute_uri() + id
      return response
    else:
      response = Response(serializer_user.erros, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
      return response