from django import forms
from home.models import Carousel
from django_summernote.widgets import SummernoteWidget

class BannerForm(forms.ModelForm):
    class Meta:
        model = Carousel
        fields = '__all__'
        widgets = {
            'image': forms.ClearableFileInput(attrs={'accept':'image/*',}),
            'title': forms.TextInput(attrs={'class':'form-control',}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'widget': SummernoteWidget()}),
            'button_name': forms.TextInput(attrs={'class':'form-control',}),
            'link': forms.URLInput(attrs={'class':'form-control',}),
        }
