from django import forms


class editImageForm(forms):
    photo = forms.ImageField()
    grayScale = forms.BooleanField()
