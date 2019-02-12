from django.shortcuts import render
from .forms import EditImageForm
from PIL import Image
from blog.models import Picture, Post
import uuid, random

def makeName():
	maxRandom = 500
	return str(uuid.getnode()) + '-' + str(random.randint(0, 500)) + ".png"

def show(request):
	form = EditImageForm(request.POST, request.FILES)

	if form.is_valid():
		photo = Image.open(request.FILES['photo'])
		if 'grayScale' in request.POST:
			photo = photo.convert('LA')

		if request.POST['left'] != "" or request.POST['right'] != "" or request.POST['up'] != "" or request.POST[
			'down'] != "":

			if request.POST['left'] == "" or request.POST['right'] == "" or request.POST['up'] == "" or \
					request.POST['down'] == "":
				return render(request, 'editImage/home.html',
							  {'form': form, 'error': 'Not valid data for crop !'})
			maxWidth, maxHeight = photo.size
			left = int(request.POST['left'])
			right = int(request.POST['right'])
			up = int(request.POST['up'])
			down = int(request.POST['down'])

			if left < 0 or up < 0 or left >= right or up >= down or right > maxWidth or down > maxHeight:
				return render(request, 'editImage/home.html', {'form': form, 'error': 'Not valid data for crop !'})

			photo = photo.crop((left, up, right, down))

		if request.POST['width'] != "" or request.POST['height'] != "":
			if request.POST['width'] == "" or request.POST['height'] == "":
				return render(request, 'editImage/home.html',
							  {'form': form, 'error': 'Not valid data for resize !'})
			width = int(request.POST['width'])
			height = int(request.POST['height'])
			if width <= 0 or height <= 0:
				return render(request, 'editImage/home.html',
							  {'form': form, 'error': 'Not valid data for resize !'})
			photo = photo.resize((width, height))

		if request.POST['rotate'] != "":
			rotate = float(request.POST['rotate'])
			photo = photo.rotate(rotate)

		name = str(uuid.getnode()) + ".png"
		photo.save("djangoTest/media/" + name)

		return render(request, 'editImage/home.html', {'form': form, 'photoUrl': name})
	return render(request, 'editImage/home.html', {'form': form})


def share(request):
	form = EditImageForm(request.POST, request.FILES)
	if form.is_valid():
		photo = Image.open(request.FILES['photo'])
		if 'grayScale' in request.POST:
			photo = photo.convert('LA')

		if request.POST['left'] != "" or request.POST['right'] != "" or request.POST['up'] != "" or request.POST[
			'down'] != "":

			if request.POST['left'] == "" or request.POST['right'] == "" or request.POST['up'] == "" or \
					request.POST['down'] == "":
				return render(request, 'editImage/home.html',
							  {'form': form, 'error': 'Not valid data for crop !'})
			maxWidth, maxHeight = photo.size
			left = int(request.POST['left'])
			right = int(request.POST['right'])
			up = int(request.POST['up'])
			down = int(request.POST['down'])

			if left < 0 or up < 0 or left >= right or up >= down or right > maxWidth or down > maxHeight:
				return render(request, 'editImage/home.html', {'form': form, 'error': 'Not valid data for crop !'})

			photo = photo.crop((left, up, right, down))

		if request.POST['width'] != "" or request.POST['height'] != "":
			if request.POST['width'] == "" or request.POST['height'] == "":
				return render(request, 'editImage/home.html',
							  {'form': form, 'error': 'Not valid data for resize !'})
			width = int(request.POST['width'])
			height = int(request.POST['height'])
			if width <= 0 or height <= 0:
				return render(request, 'editImage/home.html',
							  {'form': form, 'error': 'Not valid data for resize !'})
			photo = photo.resize((width, height))

		if request.POST['rotate'] != "":
			rotate = float(request.POST['rotate'])
			photo = photo.rotate(rotate)

		name = makeName()
		photo.save("djangoTest/media/media_photo/" + name)


		mdl = Picture()

		pst = Post.objects.first()
		mdl.post = pst
		mdl.photo = '/media_photo/' + name
		mdl.save()

		return render(request, 'editImage/home.html', {'form': form, 'sucess': 'Your photo tamam tamam !'})
	return render(request, 'editImage/home.html', {'form': form})

def home(request):
	print(uuid.getnode())
	if request.method == 'POST':
		for value in request.POST:
			print(value)

		if 'showPhoto' in request.POST:
			return show(request)

		if 'submitShare' in request.POST:
			return share(request)

	form = EditImageForm()
	form.setImage('/photo.png')
	return render(request, 'editImage/home.html', {'form': form})


