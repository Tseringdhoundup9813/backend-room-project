from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	image = models.ImageField(upload_to ="image")
	def __str__(self):
		return f'{self.user.username} Profile {self.id} id'

class Room(models.Model):
	ROOM_CHOICE =[
	('room','ROOM'),
	('apartment','APARTMENT'),
	('hostel',"HOSTEL"),
	]
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	image = models.ImageField(upload_to ="image")
	title = models.CharField(max_length=40,choices=ROOM_CHOICE)
	price = models.IntegerField(default=0)
	des = models.TextField()
	time = models.DateTimeField(auto_now_add=True)
	
	



