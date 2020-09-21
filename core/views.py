from django.shortcuts import render, redirect
from . models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def signup(request):

    if request.method == 'POST':
        Username = request.POST['username']
        Password= request.POST['password']
        Email = request.POST['email']



        try:
            User.objects.get(email=Email)
            return render(request, 'signup.html', {'error': 'this user already exists'})
        except:
            user = User.objects.create_user(email=Email, password=Password, username=Username)
            user.save()
            return redirect('login')
    return render(request, 'signup.html')

def Login(request):
    if request.method=='POST':
        Password = request.POST.get('password'),
        Email = request.POST.get('email')
        user = authenticate(request,email=Email, password=Password)

        if user is not None:
            login(request, user)
            return redirect('note')
        else:
            return render(request, 'login.html', {'error': 'either email or password is wrong'})

    return render(request, 'login.html')

@login_required
def log_out(request):
    logout(request)
    return redirect('login')
