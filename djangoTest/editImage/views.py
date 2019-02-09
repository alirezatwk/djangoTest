from django.shortcuts import render, redirect
from .forms import EditImageForm
from PIL import Image

def home(request):
	if request.method == 'POST':

		form = EditImageForm(request.POST, request.FILES)

		for value in request.POST:
			print(value)

		if form.is_valid():
			photo = Image.open(request.FILES['photo'])
			photo.show()
			print("SAAAAAAAAAAAG")
		return render(request, 'editImage/home.html', {'form': form})

		if 'showPhoto' in request.POST:

			# AGE YE FILE II UPLOAD SHOD
			if 'photo' in request.FILES:
				# AGE AKS BOD
				try:
					photo = Image.open(request.FILES['photo'])

					if 'grayScale' in request.POST:
						photo = photo.convert('LA')


					photo.save("djangoTest/media/photo.png") # TODO ESME AKSA
					return render(request, 'editImage/home.html', {'form': form, 'photoUrl': "photo.png"})
				# AGE NABOD
				except:
					print("mashti nistia")




		"""if form.is_valid():
			print("SAG MASAB\n\n")
			photo = Image.open(form.cleaned_data['photo'])
			print(photo.getpixel((0, 0)))
			grayScale = form.cleaned_data['grayScale']
			print(grayScale)
			photo.show()
			print(3)"""


	form = EditImageForm()
	return render(request, 'editImage/home.html', {'form': form})


