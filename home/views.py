from django.shortcuts import render,redirect,get_object_or_404
from .models import Room,Profile
from .forms import *
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def home(request):
	room = Room.objects.all()

	roomfilter =request.GET.get('search')
	print(roomfilter)
	if roomfilter:
		room = Room.objects.filter(title__icontains=roomfilter)

	roomcircle =request.GET.get('room')
	print(roomcircle)
	if roomcircle:
		room = Room.objects.filter(title_icontains='room')


	context ={'room':room}
	return render(request,'home.html',context);


def profile(request):
	if request.method =="POST":
		image = ProfileUpdateForm(request.POST,request.FILES)
		if image.is_valid():
			newimage = image.save(commit=False)
			newimage.user = request.user
			newimage.save()
			return redirect('home:profile')
	else:
		image = ProfileUpdateForm()


	context ={'image':image}
	return render(request,'profile.html',context)

def post(request):
	if request.method =="POST":
		post = PostForm(request.POST,request.FILES)
		if post.is_valid():
			newpost=post.save(commit=False)
			newpost.user = request.user;
			newpost.save()
			messages.success(request,'successfully created')

			return redirect('home:home')
	else:
		newpost = PostForm()


	context ={'post':newpost}
	return render(request,'post.html',context)