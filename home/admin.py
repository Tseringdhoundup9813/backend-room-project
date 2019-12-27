from django.contrib import admin

# Register your models here.
from .models import Room,Profile

admin.site.register(Room)
admin.site.register(Profile)