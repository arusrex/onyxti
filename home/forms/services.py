from django import forms
from home.models import Services, ServicesItems
from django_summernote.widgets import SummernoteWidget

class ServicesForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control',}),
            'description': SummernoteWidget(),
        }

class ServicesItemsForm(forms.ModelForm):
    class Meta:
        model = ServicesItems
        fields = '__all__'
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class':'form-control', 'accept':'image/*',}),
            'title': forms.TextInput(attrs={'class':'form-control',}),
            'link': forms.URLInput(attrs={'class':'form-control',}),
        }