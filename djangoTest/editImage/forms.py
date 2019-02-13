from django import forms

class EditImageForm(forms.Form):
    photo = forms.ImageField(required=False)

    grayScale = forms.BooleanField(required=False)

    #Crop
    left = forms.IntegerField(required=False)
    right = forms.IntegerField(required=False)
    up = forms.IntegerField(required=False)
    down = forms.IntegerField(required=False)

    #Resize
    width = forms.IntegerField(required=False)
    height = forms.IntegerField(required=False)

    rotate = forms.FloatField(required=False)
