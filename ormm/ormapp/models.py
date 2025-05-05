from django.db import models
from django.contrib import admin
class Movie (models.Model):
    User_id=models.IntegerField(primary_key=True)
    User_name=models.CharField(max_length=100)
    email=models.EmailField()
    Movie_name=models.CharField(max_length=100)
    No_of_seats=models.IntegerField()
    
 
class UserID(admin.ModelAdmin):
    list_display=('User_id','User_name','email','Movie_name','No_of_seats')