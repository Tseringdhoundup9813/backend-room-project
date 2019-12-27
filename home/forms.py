from django import forms
from .models import Profile,Room
from django.contrib.auth.models import User

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields =['first_name','last_name','username']


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields =['image']


class PostForm(forms.ModelForm):
	class Meta:
		model = Room
		fields =['title','image','des','price']