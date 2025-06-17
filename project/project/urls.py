"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('python',views.sample,name='sample'),
    path('sample1',views.sample1,name='sample1'),
    path('sample2',views.sample2,name='sample2'),
    path('sample3',views.sample3,name='sample3'),
    path('sample4',views.sample4,name='sample4'),
    path('sample5',views.sample5,name='sample5'),
    path('sample6',views.sample6,name='sample6'),
    path('form',views.form,name='form'),
    path('bonus/', views.bonus_view, name='bonus'),
    path('electricity',views.electricity,name='electricity'),
    path('dayname/', views.day_name, name='day_name'),
    path('monument/', views.city_monument, name='city_monument'),
    path('check-last-digit/', views.check_last_digit, name='check_last_digit'),
    path('bike-tax/', views.bike_tax_view, name='bike_tax'),
    path('students',views.students, name='students'),
    path('open_std/<id>',views.open_student,name='openstudent'),
    path('edit_std/<id>',views.edit_std,name='edit'),
    path('delete_std/<id>',views.delete_std,name='delete'),
    path('add_std',views.add_std,name='add_std'),
    path('',include('app.urls'))

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)



    
    





