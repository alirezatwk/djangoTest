from django.shortcuts import render
from .forms import EditImageForm
from PIL import Image
from blog.models import Picture, Post
import uuid, random

def makeName(request):
	maxRandom = 500
	return str(request.session.session_key) + '-' + str(random.randint(0, maxRandom)) + ".png"

def getName(request):
	return str(request.session.session_key) + ".png"

def havePhoto(request):
	try:
		photo = Image.open("djangoTest/media/" + getName(request))
		return True
	except:
		return False

def numberOfFields(request, attr):
	count = 0
	for str in attr:
		if request.POST[str] != "":
			count += 1
	return count

def numberOfCropFields(request):
	attr = ['left', 'right', 'up', 'down']
	return numberOfFields(request, attr)

def numberOfResizeFields(request):
	attr = ['width', 'height']
	return numberOfFields(request, attr)

def hasGrayScale(request):
	if 'grayScale' in request.POST:
		return True
	return False

def hasRotate(request):
	if request.POST['rotate'] != "":
		return True
	return False

def getCropError(request):
	count = numberOfCropFields(request)
	if count == 0:
		return ""
	if 0 < count and count < 4:
		return "You must fill all the crop fields !"
	left = int(request.POST['left'])
	right = int(request.POST['right'])
	up = int(request.POST['up'])
	down = int(request.POST['down'])
	if 'photo' in request.FILES:
		photo = Image.open(request.FILES['photo'])
	else:
		photo = Image.open("djangoTest/media/" + getName(request))
	width, height = photo.size
	if left >= right or \
		up >= down:
		return "Values must be like this 0 <= left < right < width and 0 <= up < down < height"
	if left < 0 or width <= right or \
		up < 0 or height <= down:
		return "Values must be like this 0 <= left < right < width and 0 <= up < down < height"
	return ""

def getResizeError(request):
	count = numberOfResizeFields(request)
	if count == 0:
		return ""
	if count == 1:
		return "You must fill all the resize fields !"
	width = int(request.POST['width'])
	height = int(request.POST['height'])
	if width <= 0 or \
		height <= 0:
		return "Values of resize must be positive"
	return ""

def getNotFileError(request):
	if havePhoto(request) == False and 'photo' not in request.FILES:
		return "No photo uploaded !"
	return ""

def hasError(request):
	if getNotFileError(request) != "":
		return True
	if getCropError(request) != "" or getResizeError(request) != "":
		return True
	return False

def getError(request):
	if getNotFileError(request) != "":
		return getNotFileError(request)
	if getCropError(request) != "":
		return getCropError(request)
	if getResizeError(request) != "":
		return getResizeError(request)
	return ""

def saveOriginalImage(request):
	photo = Image.open(request.FILES['photo'])
	photo.save("djangoTest/media/" + getName(request))

def editPhoto(request, photo):
	if hasGrayScale(request):
		photo = photo.convert('LA')
	if numberOfCropFields(request) != 0:
		left = int(request.POST['left'])
		right = int(request.POST['right'])
		up = int(request.POST['up'])
		down = int(request.POST['down'])
		photo = photo.crop((left, up, right, down))
	if numberOfResizeFields(request) != 0:
		width = int(request.POST['width'])
		height = int(request.POST['height'])
		photo = photo.resize((width, height))
	if hasRotate(request):
		rotate = float(request.POST['rotate'])
		photo = photo.rotate(rotate)
	return photo

def share(request, photo):
	name = makeName(request)
	photo.save("djangoTest/media/media_photo/" + name)

	if not Post.objects.filter(key=request.session.session_key).exists():
		pst = Post(key=request.session.session_key)
		pst.save()
	else:
		pst = Post.objects.get(key=request.session.session_key)

	mdl = Picture(post=pst, photo='/media_photo/' + name)
	mdl.save()

def home(request):
	if not request.session.session_key:
		request.session.create()

	uploadMessage = "Upload and edit your photo !"
	if havePhoto(request):
		uploadMessage = "We have your last photo ! Just for a new photo use upload !"

	emptyForm = EditImageForm()
	if request.method == 'POST':
		if hasError(request):
			return render(request, 'editImage/home.html', {'form': emptyForm, 'uploadMessage': uploadMessage, 'error': getError(request)})

		form = EditImageForm(request.POST, request.FILES)
		if form.is_valid() == False:
			return render(request, 'editImage/home.html', {'form': form, 'uploadMessage': uploadMessage})

		if 'photo' in request.FILES:
			saveOriginalImage(request)

		uploadMessage = "We have your last photo ! Just for a new photo use upload !"

		photo = Image.open("djangoTest/media/" + getName(request))
		photo = editPhoto(request, photo)

		name = makeName(request)
		photo.save("djangoTest/media/" + name)

		success = ""
		if 'submitShare' in request.POST:
			success = "Your photo shared !"
			share(request, photo)
		return render(request, 'editImage/home.html', {'form': form, 'success': success, 'uploadMessage': uploadMessage, 'photoUrl': name})

	return render(request, 'editImage/home.html', {'form': emptyForm, 'uploadMessage': uploadMessage})
