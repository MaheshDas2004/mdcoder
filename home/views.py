from django.shortcuts import render
from accounts.models import DarexUser
# Create your views here.
def home(request):
    
    return render(request, "home/home.html")
# return render(request,"home/home.html")