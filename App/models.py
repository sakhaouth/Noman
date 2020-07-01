from django.db import models

# Create your models here.
import datetime
from django.utils.timezone import now


class MyData(models.Model):
    name = models.CharField(max_length=50,null=False)
    email = models.EmailField(max_length=50, unique=True,null=False)
    password = models.CharField(max_length=100,null=False)
    verification_code = models.CharField(max_length=10,null=False,default='123')
    date = models.DateTimeField(default=now)

    class Meta:
        db_table = "User"
