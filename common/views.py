from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

loginUrl = '/admin/login/'


# Create your views here.
# Home Navigation------------------------------------------------------------------------------------------
@login_required(login_url=loginUrl)
def home(request):
    return render(request, 'Home/home.html')
