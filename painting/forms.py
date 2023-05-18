from django import forms 
from .models import Painting

class PaintingForm(forms.ModelForm):
    class Meta:
        model = Painting
        fields = '__all__'

class PaintingUploadForm(forms.ModelForm):
    class Meta:
        model = Painting
        fields = ['name', 'description','image']

