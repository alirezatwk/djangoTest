from django import forms

class EditImageForm(forms.Form):
    photo = forms.ImageField()
    grayScale = forms.BooleanField(required=False)
    left = forms.IntegerField(required=False)
    right = forms.IntegerField(required=False)
    up = forms.IntegerField(required=False)
    down = forms.IntegerField(required=False)
    width = forms.IntegerField(required=False)
    height = forms.IntegerField(required=False)
    rotate = forms.FloatField(required=False)