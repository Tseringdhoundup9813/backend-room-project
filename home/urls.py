from django.urls import path

from .import views

app_name ="home"

urlpatterns = [
	path('',views.home,name='home'),
	path('profile/',views.profile,name='profile'),
	path('post/',views.post,name='post'),
]