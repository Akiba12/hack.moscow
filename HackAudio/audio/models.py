from django.db import models
from django.contrib.auth.models import User
import datetime

class data(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.CharField(max_length=50)
    message_id = models.CharField(max_length=100)
    text = models.TextField()
    sender = models.CharField(max_length=100)
    date = models.DateField(("Date"), default=datetime.date.today)
    readed = models.BooleanField(default=False)


class services(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vk = models.CharField(max_length=500, default="NULL")
    instagram = models.CharField(max_length=500, default="NULL")
    telegram = models.CharField(max_length=500, default="NULL")
    whatsapp = models.CharField(max_length=500, default="NULL")