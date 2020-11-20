from django import forms
from .models import *

class Pic(forms.ModelForm):

	class Meta:
		model = Post
		fields = ['image']