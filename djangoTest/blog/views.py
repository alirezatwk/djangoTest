from django.shortcuts import render
from .models import Post, Picture


def home(request):
	context = {
		'posts': Post.objects.all(),
		'pictures': Picture.objects.all(),
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})