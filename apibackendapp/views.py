from django.shortcuts import render
from rest_framework import viewsets
from .models import Employee,department
from django.contrib.auth.models import User
from .serializers import EmployeeSerializer,DepartmentSerializer,UserSerializer,SignupSerializer
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate

class signupAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self,request):
        serializer = SignupSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created =  Token.objects.get_or_create(user=user)
            return Response({
                "user_id" : user.id,
                "username" : user.username,
                "token" : token.key,
                "role" : user.groups.all()[0].id if user.groups.exists() else None},
                status=status.HTTP_201_CREATED)
        else:
            response = {'status':status.HTTP_400_BAD_REQUEST, 'data':serializer.errors}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        
class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self,request):
        serializer = SignupSerializer(data = request.data)
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                token = Token.objects.get(user=user)
                response = {
                    "status":status.HTTP_200_OK,
                    "message":"success",
                    "username": user.username,
                    "role":user.groups.all()[0].id if user.groups.exists() else None,
                    "data":{
                        "Token":token.key
                    }

                }
                return Response(response, status=status.HTTP_200_OK)


            else:
                response = {
                    "status": status.HTTP_401_UNAUTHORIZED,
                    "message" : "Inavlid username or password",
                
                }
                return Response(response, status=status.HTTP_401_UNAUTHORIZED,)#login failed
        else:
            response = {'status':status.HTTP_400_BAD_REQUEST, 'data':serializer.errors}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

            

    





class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = department.objects.all()#get the all objects of the model
    serializer_class = DepartmentSerializer
    # permission_classes = []
    permission_classes =[IsAuthenticated]


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()#get the all objects of the model
    serializer_class = EmployeeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['EmployeeName','Desigination']
    permission_classes = []
    # permission_classes =[IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()#get the all objects of the model
    serializer_class = UserSerializer
    # permission_classes = []
    permission_classes =[IsAuthenticated]

