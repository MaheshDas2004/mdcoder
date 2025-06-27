from django.http import HttpResponse
from django.shortcuts import render, redirect

def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")
def profile(request):
    return render(request,"profile.html")

def categories(request):
    return render(request,"categories.html")

def browsedares(request):
    return render(request,"browsedares.html")

def login(request):
    if request.method=='POST':
        username=request.POST.get("username")
        password=request.POST.get("password")
        
        print("username: ",username)
        print("password: ",password)
        request.session['username']=username
        return redirect('home')
    return render(request,"login.html")
def logout(request):
    request.session.flush()
    return redirect ("home")

def signup(request):
    if(request.method=='POST'):
        username=request.POST.get("username")
        password=request.POST.get("password")
        confirm_password=request.POST.get("confirm_password")
        email=request.POST.get("email")
        if password==confirm_password:
            request.session['username']=username
            request.session['loggedin']=True
            print(request.POST)
            return redirect("home")
        else:
            return render(request,"signup.html",{"error": "Passwords do not match"})
            print("botht the passwords dont match")
    return render(request,"signup.html")
