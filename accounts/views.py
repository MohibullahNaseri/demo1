from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if User.objects.filter(username=username):
            messages.info(request, 'Username is Taken')
            return redirect('register')
        elif User.objects.filter(email=email):
            messages.info(request, 'Email already exist!')
            return redirect('register')
        elif password1 != password2:
            messages.info(request, 'Password Not Matching ..')
            return redirect('register')
        else:
            user = User.objects.create_user(username=username,
                                            email=email,
                                            first_name=first_name,
                                            last_name=last_name,
                                            password=password1)
            user.save()
            return redirect('login')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credential')
            return redirect('login')
    else:
        return render(request, 'login.html')


@login_required()
def logout(request):
    # if request.user.is_authenticated:
    auth.logout(request)
    return redirect('/')

# else:
# messages.info(request, 'Please login')
# return redirect('login')


