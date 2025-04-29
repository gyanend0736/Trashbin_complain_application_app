from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from login.forms import Signup
from django.contrib.auth.models import User
from django.contrib.auth import logout
from login.models import Complaint

def signup_view(request):
    if request.method == 'POST':
        form = Signup(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, "Registered Successfully!!")
            return redirect(login_view)  # after signup, go to login page
    else:
        form = Signup()
    return render(request, "login.html", {"form": form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)  # correct way
            messages.success(request, f"Welcome {username}!")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, "login.html")
    return render(request, 'login.html')
def logout_view(request):
    logout(request)
    return redirect(home)

def home(request):
    return render(request, 'home.html')

def complaint_view(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        address= request.POST.get('address')
        areacode= request.POST.get('Areacode')
        if text:
            Complaint.objects.create(user=request.user, text=text,address=address,areacode=areacode)
            return redirect('home')
    return render(request, 'complaint.html')