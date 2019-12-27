from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def register(request):
	if request.method =="POST":
		register = UserRegistrationForm(request.POST)
		if register.is_valid():
			first_name =register.cleaned_data['first_name']
			last_name =register.cleaned_data['last_name']
			username = register.cleaned_data['username']
			password = register.cleaned_data['password']
			user = User.objects.create_user(username,first_name=first_name,last_name=last_name,password=password)
			messages.success(request,'Registration is success {}'.format(username))
			return redirect('home:home')
		else:
			messages.error(request,'user is not created')
	else:
		register = UserRegistrationForm()
	context= {'register':register}
	return render(request,'register.html',context);


def login_user(request):
	if request.method =="POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request,username=username,password=password)
		if user:
			login(request,user)
			return redirect('home:home')
			messages.success(request,'you are log in now {}'.format(username))
		else:
			messages.error(request,'username or password is bad')

	return render(request,'login.html');


def logout_user(request):
	logout(request)
	return redirect('home:home')