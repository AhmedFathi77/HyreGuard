from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.
class CreateUser(AbstractBaseUser):
	Provider = 'P'
	Seeker   = 'S'
	CHOICES = ((Provider, 'Provider'), (Seeker, 'Seeker'))
	FirstName   = models.CharField(max_length=50)
	LastName    = models.CharField(max_length=50)
	Email       = models.EmailField(unique=True)
	Pass    	= models.CharField(max_length=50)
	Country     = models.CharField(max_length=50)
	State	    = models.CharField(max_length=50)
	City	    = models.CharField(max_length=50)
	Company	    = models.CharField(max_length=50)
	Date	    = models.DateField(default=date.today)
	Is_Staff	= models.BooleanField(null=True)
	Is_Active	= models.BooleanField(null=True)
	Acc_Type	= models.CharField(max_length=1 , choices=CHOICES ,null=True)

	def __str__(self):
		return self.FirstName + ' ' + self.LastName


