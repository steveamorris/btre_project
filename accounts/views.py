from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User



# Create your views here.

def register(request):
  if request.method == 'POST':
    # Get Form Values
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    # Check if passowrds match
    if password == password2:
      if User.objects.filter(username=username).exists():
        messages.error(request, 'Username exists')
        return redirect('register')
      else:
        if User.objects.filter(email=email).exists():
          messages.error(request, 'Email exists')
          return redirect('register')
        else:
          user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
          # Log user in
          # auth.login(request, user)
          # messages.success(request, 'You are now logged in')
          # return redirect('index')

          # Make user log in
          user.save()
          messages.success(request, 'You are now registered and can log in')
          return redirect('login')
    else:
      messages.error(request, 'Passwords do not match')
      return redirect('register')
  else:
    return render(request, 'accounts/register.html')

def login(request):
  if request.method == 'POST':
    print('Submitted')
    return redirect('register')
  else:
    return render(request, 'accounts/login.html')

def logout(request):
  return redirect('index')

def dashboard(request):
  return render(request, 'accounts/dashboard.html')