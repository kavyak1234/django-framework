from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import student
from django.contrib import messages
from django.contrib.auth.models import User




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
def bonus_view(request):
    bonus = None
    salary = None
    years = None
    if request.method == 'POST':
        salary = float(request.POST.get('salary'))
        years = int(request.POST.get('years'))

        if years > 5:
            bonus = salary * 0.05
        else:
            bonus = 0
    return render(request, 'bonus.html', {'bonus': bonus, 'salary': salary, 'years': years})
def electricity(request):
    bill = None

    if request.method == 'POST':
        units_input = request.POST.get('units')
        if units_input:  
            units = int(units_input)

            if units <= 100:
                bill = 0
            elif units <= 200:
                bill = (units - 100) * 5
            else:
                bill = (100 * 5) + (units - 200) * 10

    return render(request, 'electricity.html', {'bill': bill})

def day_name(request):
    day = ''
    if request.method == 'POST':
        number = int(request.POST.get('number'))
        days = {
            1: 'Sunday',
            2: 'Monday',
            3: 'Tuesday',
            4: 'Wednesday',
            5: 'Thursday',
            6: 'Friday',
            7: 'Saturday'
        }
        day = days.get(number, 'Invalid number! Please enter between 1 and 7.')
    return render(request, 'dayname.html', {'day': day})

def city_monument(request):
    monument = ''
    if request.method == 'POST':
        city = request.POST.get('city').strip().lower()
        city_monuments = {
            'delhi': 'Red Fort',
            'agra': 'Taj Mahal',
            'jaipur': 'Jal Mahal'
        }
        monument = city_monuments.get(city, 'No monument found for this city.')
    return render(request, 'monument.html', {'monument': monument})

def check_last_digit(request):
    result = ''
    if request.method == 'POST':
        number = request.POST.get('number')
        if number.isdigit():  
            last_digit = int(number[-1])
            if last_digit % 3 == 0:
                result = f"The last digit {last_digit} is divisible by 3."
            else:
                result = f"The last digit {last_digit} is NOT divisible by 3."
        else:
            result = "Please enter a valid number."
    return render(request, 'last_digit_check.html', {'result': result})


def bike_tax_view(request):
    tax = None
    cost = None
    if request.method == 'POST':
        cost = float(request.POST.get('cost_price'))
        if cost > 100000:
            tax = cost * 0.15
        elif cost > 50000:
            tax = cost * 0.10
        else:
            tax = cost * 0.05
    return render(request, 'bike_tax.html', {'tax': tax, 'cost': cost})

def students(request):
    data = student.objects.all()
    return render(request,'shop.html',{'students': data})


def open_student(request,id):
    print(id)
    data = student.objects.get(pk=id)
    print(data)
    return render(request,'open_std.html',{'student':data})
def edit_std(request,id):
    data = student.objects.get(pk=id)
    if request.method == 'POST':
        data.Rollno = request.POST['Rollno']
        data.Name = request.POST['Name']
        data.Email = request.POST['Email']
        data.Age = request.POST['Age']
        if request.FILES:
             data.Image = request.FILES['Image']
        data.save()
        return redirect(students)
    return render(request,'edit.html',{'student':data})
def delete_std(request,id):
        data = student.objects.get(pk=id)
        data.delete()
        return redirect(students)
def add_std(request):
    if request.method=='POST':
        roll = request.POST['Rollno']
        name =  request.POST['Name']
        email = request.POST['Email']
        age = request.POST['Age']
        image =request.FILES['Image']
        data = student.objects.create(Rollno=roll,Email=email,Name=name,Age=age,Image=image)
        data.save()
        return redirect(students)
    return render(request,'add_std.html')

def user_login(request):
    return render(request,'login.html')
def user_registration(request):
    if request.method =='POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        data = User.objects.create_user(username=email,password=password,email=email,first_name=name)
        data.save()
        messages.success(request, "Registration completed.")
        return redirect('login')
    return render(request,'register.html')
def user_home(request):
    return render(request,'home.html')



