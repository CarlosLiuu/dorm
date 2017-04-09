from django.db import models

# Create your models here.

class User(models.Model):
	username = models.IntegerField(blank=False,unique=True)
	number = models.IntegerField()
	name = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	email = models.EmailField()
	def __str__(self):
		return self.username