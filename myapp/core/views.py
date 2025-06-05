from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def sample6(request):
    print("hello its me kavya")
    return HttpResponse("hello its me kavya")
def sample3(req):
    a=5
    b=10
    c=20
    return render(req,'sample6.html',{'data':a, 'data1':b})




