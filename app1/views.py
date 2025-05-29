from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def homepage(request):
    return render(request,'index.html')


def hospital_form(request):
    if request.method =='POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        mobile_no=request.POST.get('mobile_no')
       
        hospital.objects.create(name=name,age=age,gender=gender,mobile_no=mobile_no)
        return redirect('hospital_form')
    hospitals=hospital.objects.all()
    return render(request,'hospital.html',{'hospitals':hospitals})
 

def signup_view(request):
    if request.method == 'POST':
       username = request.POST.get('username')
       email = request.POST.get('email')
       password = request.POST.get('password')

       if User.objects.filter(username=username).exists():
          messages.error(request, "Username already exists.")
          return redirect('singup')

       user = User.objects.create_user(username=username, email=email, password=password)
       messages.success(request, "account created successfully.")
       return redirect('login')

    return render(request,'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('hospital_form')    
        else:
            messages.error(request,"invalid credientials")
            return redirect('login')

    return render(request, 'login.html') 

def logout_view(request):
    logout(request)
    return redirect('login')       

def client_form(request):
     if request.method =='POST':
        patient_code=request.POST.get('patient_code')
        patient_name=request.POST.get('patient_name')
        age=request.POST.get('age')
        dob=request.POST.get('dob')
        gender=request.POST.get('gender')
        father_name=request.POST.get('father_name')
        husband_name=request.POST.get('husband_name')
        disease=request.POST.get('disease')
        blood_group=request.POST.get('blood_group')
        address=request.POST.get('address')
        mobile_no=request.POST.get('mobile_no')
        email=request.POST.get('email')
         

        client.objects.create(patient_code=patient_code,patient_name=patient_name,age=age,dob=dob,gender=gender,
                                father_name=father_name,husband_name=husband_name,disease=disease,blood_group=blood_group,
                                address=address,mobile_no=mobile_no,email=email)
        return redirect('hospital_client')
     clients=client.objects.all()
     return render(request,'client.html',{'clients':clients})


def edit_client(request, pk):
    clients = get_object_or_404(client, pk=pk)

    if request.method == "POST":
        patient_name=request.POST.get('patient_name')
        gender=request.POST.get('gender')
        blood_group=request.POST.get('blood_group')
        clients.save()
        return redirect("edit_client")

    return render(request,"edit.html", {
        "edit_client": client,
        "client": client.objects.all()
    })


def delete_client(request, pk):
    clients = get_object_or_404(client, pk=pk)
    clients.delete()
    return redirect("delete_client")
    
 