from django.db import models

class User(models.Model):
	name=models.CharField(max_length=20)
	roll_no=models.IntegerField()