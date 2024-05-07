from django.db import models
from django.contrib.auth.models import User
import uuid

class LoginPage(models.Model):
	username = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	password = models.CharField(max_length=200, null=True)
	# email = models.CharField(max_length=200)

	

class Signup(models.Model):
	username = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	password = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)
	# confirmpass = models.CharField(max_length=200, null=True)  

	def __str__(self):
		return self.name

# models.py

class Contact(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    donation = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class RegisterNgo(models.Model):
	username = models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	register = models.CharField(max_length=50)
	address = models.CharField(max_length=255)
	email = models.CharField(max_length=100)
	contact= models.CharField(max_length=100)
	weurl = models.CharField(max_length=100)

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     bio = models.TextField(blank=True)
#     website = models.URLField(blank=True)
#     phone_number = models.CharField(max_length=20, blank=True)

#     def __str__(self):
#         return f"{self.user.username}'s Profile"

	
	

    


