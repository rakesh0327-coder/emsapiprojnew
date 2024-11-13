from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path

#create a instance of the DefaultRputer 
router = DefaultRouter()


router.register(r'departments', views.DepartmentViewSet)
router.register(r'employees', views.EmployeeViewSet)
router.register(r'users', views.UserViewSet)


#creating url's for the login and Signup api views
urlpatterns = [
    path("signup/",views.signupAPIView.as_view(),name="user-signup"),
    path("login/",views.signupAPIView.as_view(),name="user-login"),
    
]

urlpatterns = urlpatterns + router.urls




