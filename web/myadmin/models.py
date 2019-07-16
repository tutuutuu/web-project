from django.db import models

# Create your models here.


class User(models.Model):
	username = models.CharField(max_length=20, null=True)
	password = models.CharField(max_length=77)
	phone = models.CharField(max_length=11)
	email = models.CharField(max_length=100)
	age = models.IntegerField(null=True)
	pic_url = models.CharField(max_length=100)
	SEX_CHOICES = (
		(0, '女'),
		(1, '男'),
	)
	sex = models.CharField(max_length=1,null=True,choices=SEX_CHOICES)
	status = models.IntegerField(default=0)
	addtime = models.DateTimeField(auto_now_add=True)


