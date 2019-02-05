from django.shortcuts import render
from .forms import EditImageForm
from PIL import Image

def home(request):
	if request.method == 'POST':



		if 'showPhoto' in request.POST:

			# AGE YE FILE II UPLOAD SHOD
			if 'photo' in request.FILES:
				# AGE AKS BOD
				try:
					photo = Image.open(request.FILES['photo'])
					print("HAHAH")
				# AGE NABOD
				except:
					print("mashti nistia")


		for value in request.POST:
			print(value)


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


