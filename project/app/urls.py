from django.urls import path
from .import views

urlpatterns = [
    path('login',views.user_login,name='login'),
    path('',views.user_home,name='home'),
    path('register',views.user_registration,name='register'),
    path('logout',views.user_logout,name='logout'),
    path('add_std',views.add_std,name='add_std'),
    path('add_std1',views.add_std1,name='add_std1'),
    path('viewpost',views.viewpost,name='post')

]
