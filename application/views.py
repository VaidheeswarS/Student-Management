from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from .models import *
from django.contrib.auth import  login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    return render(request,"home.html")


def register(request):
    if request.method=="POST":
        fname=request.POST.get("stuname")
        # mname=request.POST.get("midname")
        lname=request.POST.get("lname")
        School=request.POST.get("school_name")
        std=request.POST.get("std")
        section=request.POST.get("sec")
        dob=request.POST.get("dob")
        age=request.POST.get("age")
        phone=request.POST.get("pphone")
        gender=request.POST.get("gender")
        photo=request.POST.get("S_photo")
        email=request.POST.get("email")
        password=request.POST.get("password")

        students_info.objects.create(First_Name=fname,Last_Name=lname,School=School,STD=std,section=section,D_O_B=dob,Age=age,Parents_Phone_Number=phone,Gender=gender,Email_id=email,Photo=photo,Password=password)
        
        dbdata=get_object_or_404(students_info,Email_id=email)
        
        print(dbdata.First_Name)
        print(dbdata)
        return render(request,"view.html",{"datas":dbdata})
        # return render(request,"view.html",{"fname":fname,"mname":mname,"lname":lname,"School":School,"std":std,"section":section,"dob":dob,"age":age,"gender":gender,"phone":phone,"email":email,"password":password,"photo":photo})
    return render(request,"registration.html")

# @login_required
def update(request,value):
    obj=get_object_or_404(students_info,Email_id=value)
    if request.method=="POST":
        fname=request.POST.get("stuname")
        # mname=request.POST.get("midname")
        lname=request.POST.get("lname")
        School=request.POST.get("school_name")
        std=request.POST.get("std")
        section=request.POST.get("sec")
        dob=request.POST.get("dob")
        age=request.POST.get("age")
        phone=request.POST.get("pphone")
        gender=request.POST.get("gender")
        photo=request.POST.get("S_photo")
        email=request.POST.get("email")
        password=request.POST.get("password")

        obj.First_Name=fname
        # obj.Mid_Name=mname
        obj.Last_Name=lname
        obj.STD=std
        obj.section=section
        obj.D_O_B=dob
        obj.Parents_Phone_Number=phone
        obj.Password=password
        obj.Photo=photo
        obj.Email_id=email
        obj.Age=age
        obj.Gender=gender
        obj.School=School
        # students_info.objects.create(First_Name=student.First_Name,Mid_Name=student.Mid_Name,Last_Name=student.Last_Name,School=student.School,STD=student.STD,section=student.section,D_O_B=student.D_O_B,Age=student.Age,Parents_Phone_Number=student.Parents_Phone_Number,Gender=student.Gender,Email_id=student.Email_id,Photo=student.Photo,Password=student.Password)
        obj.save()
        return redirect("/overallview")
    return render(request,"update.html",{"data":obj})
                
def delete(request,dvalue):
    if request.method=="POST":
        row=get_object_or_404(students_info,Email_id=dvalue)
        students_info.delete(row)   
        return HttpResponse("Profile Deleted Sucessfully !!!")


# def del2(request,val):
#     if request.method=="POST":
#         students_info.delete(val)
    
        
# @login_required
def overview(request):
    if request.method=="POST":
        pass
    else:
        print(User)
        o_data=students_info.objects.all()
        return render(request,"oview.html",{"o_value":o_data})


@login_required
def searchbar(request):
    if request.method=="POST":
        name=request.POST.get("search_value")
        # name.split(" ")
        print(name)
        person=get_object_or_404(students_info,First_Name=name)
        return render(request,"search.html",{"person":person})
    return render(request,"search.html")

def log_in(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        student=get_object_or_404(students_info,Email_id=email)
        print(student.Email_id)
        print(student.Password)
        if email==student.Email_id and password==student.Password:
            user,created=User.objects.get_or_create(email=student.Email_id,password=student.Password)
            user.save()
            login(request,user)
            return redirect("/home")
    return render(request,"login.html")


@login_required
def log_out(request):
    logout(request)
    return HttpResponse("loggedout.....!")