from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sample(req):
    print("welcome")
    return HttpResponse("welcome")
def sample1(request):
    return HttpResponse("sample1")
def sample2(req):
    return HttpResponse("sample2")
def sample3(request):
    return HttpResponse("sample3")
def sample4(req):
    return HttpResponse("sample4")
def sample5(req):
    a="its a variable in sample5 function"
    b=20
    return render(req,'sample.html',{'data':a,"data1":b})
def sample6(req):
    a="its a variable in sample6 function"
    b=20
    return render(req,'sample1.html',{'data':a,"data1":b})
def form(request):
    if request.method =='POST':
        email = request.POST['email']
        phone = request.POST['phno']
        print('email',email)
        print('phno',phone)
    return render(request,'inputform.html') 
def company(request):
    if re





