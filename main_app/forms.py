from django import forms
from .models import *
from pyuploadcare.dj.forms import ImageField

class ProfileForm(forms.ModelForm):
    photo = ImageField(label='')

    class Meta: 
        model = Profile
        fields = ['name', 'location', 'bio', 'photo']


class PostForm(forms.ModelForm):
    photo = ImageField(label='')

    class Meta:
        model = Post 
        fields = ['photo']