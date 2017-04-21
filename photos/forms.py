from django import forms

from .models import Photo


class PostPhoto(forms.ModelForm):
    class Meta:
        model = Photo
        fields = [
            'title', 'image', 'commentary',
             ]
