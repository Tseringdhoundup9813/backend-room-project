
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
class UserRegistrationForm(forms.Form):
	first_name =forms.CharField(max_length=100,widget=forms.TextInput(
		attrs={'class':'username','placeholder':'enter first_name'}))
	last_name =forms.CharField(max_length=100,widget=forms.TextInput(
		attrs={'class':'username','placeholder':'enter last_name'}))
	username = forms.CharField(max_length=100,widget=forms.TextInput(
		attrs={'class':'username','placeholder':'enter username'}))
	password = forms.CharField(max_length=100,widget=forms.TextInput(
		attrs={'class':'username','placeholder':'enter password'}))
	confirm =forms.CharField(max_length=100,widget=forms.TextInput(
		attrs={'class':'username','placeholder':'enter confirm'}))


	

	def clean_username(self):
		username =self.cleaned_data['username']
		u  = User.objects.filter(username=username)
		if u.exists():
			raise ValidationError("username is already taken")
		if len(username) < 4:
			raise ValidationError('username is too short')
		return username

	def clean_confirm(self):
		p1 = self.cleaned_data['password']
		p2 = self.cleaned_data['confirm']
		if p2 != p1:
			raise ValidationError('password is not match')
		return p2
