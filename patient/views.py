from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import DoctorModel,PatientModel

# Create your views here.
error=False
user_error=False
@login_required
def Home(request):
    return render(request, 'patient/index.html')


def signUp(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        name = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        rpassword=request.POST.get('rpassword')
        val =request.POST['user']
        p=request.POST['profilepic']
        print(val)
        # val=request.POST.get('input_name')
        if(val =='doctor'):
            doctor=DoctorModel(pic=p)
            doctor.fname=fname
            doctor.lname=lname
            doctor.email=email
            doctor.uname=name
            doctor.save() 
        if(val =='patient'):
            patient=PatientModel(pic=p)
            patient.fname=fname
            patient.lname=lname
            patient.email=email
            patient.uname=name
            patient.save() 
        try:
            new_user = User.objects.create_user(name, email, password)
        except Exception as e:
            user_error=True
            return render(request,'patient/signup.html',{'user_error':user_error})
        new_user.first_name = fname
        new_user.last_name = lname
        new_user.save()
        if(password==rpassword): 
            return redirect('login-page')
        else:
            error=True
            return render(request,'patient/signup.html',{'error':error})
        
    return render(request, 'patient/signup.html')


def logIn(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('password')

        user = authenticate(username=name, password=password)
        if(user is not None):
            login(request, user)
            email_field = user.get_email_field_name()
            email = getattr(user, email_field, None)
            fullname = User.get_full_name(request.user)
            fname, lname = fullname.split(" ")
            dict={'fname':fname,'lname':lname,'email':email,'name':user.username,}
            if is_person_in_patient(user.username):
                dict['pic']=PatientModel.pic
                print(dict['pic'])
                return render(request, 'patient/dashBoardPatient.html',dict)
                
            else:
                dict['pic']=PatientModel.pic
                return render(request,'patient/dashBoardDoctor.html',dict) 
               
        else:
            error=True
            dict ={'error':error}
            return render(request,'patient/login.html',context=dict)
    return render(request, 'patient/login.html', {})


def logOut(request):
    logout(request)
    return redirect('login-page')


def Test(request):
    return render(request, 'patient/dashBoardDoctor.html')
def is_person_in_patient(name):
    print(name)
    matching_persons=PatientModel.objects.filter(uname=name)
    if matching_persons.exists():
        return True
    else:
        return False