from django.db import models
from django.contrib.auth.models import AbstractUser

class Students(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True,verbose_name="email address",
        error_messages={'unique': 'A user with that email already exists.'})
    mat_number = models.CharField(max_length=20, unique=True,error_messages={'unique': 'A user with that MatNO already exists.'})
    image = models.ImageField(blank=True, null=True, upload_to='user_DP/',default="3.jpg")
    bio = models.TextField(max_length=500, blank=True, null=True, default="Economics is the blood that runs through the vains of a country")

    def __str__(self) -> str:
        return self.username

class ResultU2018(models.Model):
    mat_number = models.CharField(max_length=20)
    year = models.IntegerField()
    semester = models.IntegerField()
    course_code = models.CharField(max_length=20)
    course_title = models.CharField(max_length=255)    
    credit_unit = models.DecimalField(max_digits=5,default=3, decimal_places=2)
    mark = models.DecimalField(max_digits=5, decimal_places=2)
    grade = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.mat_number
