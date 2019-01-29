from django.db import models
from django.utils import timezone
from PIL import Image

#from django.contrib.auth.models import User

class Post(models.Model):
	#title = models.CharField(max_length=100)
	#content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	#author = models.ForeignKey(User, on_delete=models.CASCADE)

	#def __str__(self):
		#return self.title

class Picture(models.Model):
	photo = models.ImageField(upload_to='media_photo', default="")
	post = models.ForeignKey(Post, on_delete=models.CASCADE)

