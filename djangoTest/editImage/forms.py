from django import forms

class EditImageForm(forms.Form):
    photo = forms.ImageField()
    grayScale = forms.BooleanField()