from django.urls import path
from .import views

urlpatterns = [
    path('',views.user_login,name='login'),
    path('home',views.user_home,name='home'),
    path('register',views.user_registration,name='register')

]
