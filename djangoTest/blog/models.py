from django.db import models


class Post(models.Model):
	key = models.CharField(max_length=40, default="")


class Picture(models.Model):
	photo = models.ImageField(upload_to='media_photo', default="")
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	deleted = models.BooleanField(default=False)

