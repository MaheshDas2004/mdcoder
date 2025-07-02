from django.shortcuts import render

# Create your views here.
def login(request):
    if(request.method=="POST"):
        username=request.username
        password=request.password

        #check it through database if user exists


    return render(request,"accounts/login.html")
def signup(request):
    if(request.method=='POST'):
        username=request.POST.get("username")
        email=request.email
        password=request.password
        cf_password=request.confirm_password

        if(cf_password!=password):
            error="passwords do noit match"
            return render(request,"accounts/signup.html")
    return render(request,"accounts/signup.html")