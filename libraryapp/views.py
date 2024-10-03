from django.http import HttpResponse
from django.shortcuts import render
from  .models import *


def home(request):
    return render(request,"home.html")

def login(request):
    return render(request,"login_entry.html")

def Library(request):
    return render(request,"Library.html")

def Book_entry(request):
    return render(request,"Book_entry.html")

def submit(request):
    return render(request,"Library.html")
'''
def register(request):
    return render(request,"register.html")
'''
def submit(request):
    if(request.method=="POST"):
        T1 = request.POST.get('T1')
        T2 = request.POST.get('T2')
        T3 = request.POST.get('T3')
        T4 = request.POST.get('T4')
        T5 = request.POST.get('T5')
        T6 = request.POST.get('T6')
        T7 = request.POST.get('T7')
        T8 = request.POST.get('T8')
        S1 = Bookdata(BookName=T1, Description=T2, Author=T3, Price=T4, Category=T5, Pages=T6, Date_Of_Publish=T7, Photo=T8)
        S1.save()
        return render(request,"Library.html")   
    return render(request,"Library.html")

def display(request):
    S1 = Bookdata.objects.all()
    context = {"S1":S1}
    return render(request,"display.html",context)  

def delete(request,id):
    T1 = Bookdata.objects.get(id=id)
    T1.delete()
    S1 = Bookdata.objects.all()
    context = {"S1":S1}
    return render(request,"display.html",context)


def edit(request,id):
    T1 = Bookdata.objects.get(id=id)
    context = {"T1":T1}
    return render(request,"edit.html",context)

def update(request,id):
    R1=Bookdata.objects.get(id=id)
    if(request.method == "POST"):
        T1 = request.POST.get('T1')
        T2 = request.POST.get('T2')
        T3 = request.POST.get('T3')
        T4 = request.POST.get('T4')
        T5 = request.POST.get('T5')
        T6 = request.POST.get('T6')
        T7 = request.POST.get('T7')
        T8 = request.POST.get('T8')
        R1.BookName = T1
        R1.Description = T2
        R1.Author = T3
        R1.Price = T4
        R1.Category  = T5
        R1.Pages = T6
        R1.Date_Of_Publish = T7
        R1.Photo = T8
        R1.save()
    S1 = Bookdata.objects.all()
    context = {"S1":S1}
    return render(request,"display.html",context)

def register(request):
    if(request.method=="POST"):
        Fullname = request.POST.get('Fullname')
        Username = request.POST.get('Username')
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
        DOB = request.POST.get('DOB')
        Gender = request.POST.get('Gender')
        Language = request.POST.get('Language')
        Aadhar = request.POST.get('Aadhar')
        Profilepic = request.POST.get('Profilepic')
        data = Details(Name=Fullname, Username=Username, Email=Email, Password=Password, DOB=DOB, Gender=Gender,Language=Language, Aadhar=Aadhar, Profilepic=Profilepic )
        data.save()
        return render(request,"login_entry.html")   
    return render(request,"register.html",)

def login_entry(request):
    return render(request, 'login_entry.html')
    
def login_submit(request):
    if(request.method == "POST"):
        T1 = request.POST.get('T1')
        T2 = request.POST.get('T2')
        S1 = Details.objects.all().values_list()
        flag  = 0
        for i in S1:
            if i[2] == T1 and i[4] ==   T2:
                return render(request, 'login_success.html')
                flag += 1
                break
        if flag == 0:
            return render(request, 'login_failure.html')
   
    else:
        
        return render(request, 'login.html')
    