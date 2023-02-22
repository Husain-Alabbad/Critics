from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import datetime

# Create your models here.

GENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
)
class Profile(models.Model):

    first_name = models.CharField(max_length=200, default="")
    last_name = models.CharField(max_length=200, default="")
    gender = models.CharField(max_length=50, choices=GENDER, default=GENDER[0][0])
    contact_number = models.CharField(max_length=200, default="")
    dob = models.DateField( default=datetime.date.today)
    image = models.ImageField(upload_to='main_app/static/img/profile', default="")
    favorite_tv_show = models.CharField(max_length=500, default="")
    favorite_novel = models.CharField(max_length=500, default="")
    favorite_game = models.CharField(max_length=500, default="")
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.user.username} Profile'

    def get_absolute_url(self):
        return reverse('home')
