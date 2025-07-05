from django.shortcuts import render,redirect
from . models import DarexUser
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.
def login(request):
    if(request.method=="POST"):
        context={}
        username=request.POST.get("username")
        password=request.POST.get("password")

        try:
            user = DarexUser.objects.get(username=username)
        
            if check_password(password,user.password):
                request.session["username"]=username
                request.session["loggedin"]=True
                return redirect("home")
            else:
                context["error"]="Invalid username or password"
                return render (request,"accounts/login.html",context)
        except DarexUser.DoesNotExist:
                context["error"]="Invalid username or password"

    return render(request,"accounts/login.html")

def signup(request):
    if(request.method=='POST'):
        name=request.POST.get("name")
        email = request.POST.get("email", "").strip()
        password=request.POST.get("password")
        cf_password=request.POST.get("confirm_password")
        context={
    
        }
        if(cf_password!=password):
            context["error"]="Passwords do not match Enter again"
            print("passwords do not match")
            return render(request,"accounts/signup.html",context)
        
        if DarexUser.objects.filter(email=email).exists():
            context["error"]="Email already exists"
            return render(request, 'accounts/signup.html',context)
        
        h_password= make_password(password)
        user = DarexUser.objects.create(name=name, email=email, password=h_password)

        request.session["user_id"]=user.id
        request.session["show_modal"]=True
        return redirect("home")
    
    return render(request,"accounts/signup.html")

def complete_profile(request):
    if request.method == 'POST':
        user_id = request.session.get("user_id")
        if not user_id:
            return redirect("home")

        user = DarexUser.objects.get(id=user_id)
        user.username = request.POST.get("username")
        user.college = request.POST.get("college")
        user.phone = request.POST.get("phone")
        user.save()

        request.session["username"]=user.username
        request.session.pop("show_modal", None)
        request.session["loggedin"]=True
        return redirect("home")
def profile(request):
    username=request.session.get("username")
    user=DarexUser.objects.get(username=username)

    return render(request,"accounts/profile.html",{"user":user})