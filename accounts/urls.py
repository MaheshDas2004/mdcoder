from django.contrib import admin
from django.urls import path,include

from . import views
urlpatterns = [
    path('login/',views.login, name='login'),
    path('signup/',views.signup, name='signup'),
    path('complete-profile/', views.complete_profile, name="complete_profile"),
    path('profile/', views.profile, name='profile')

]
