from django import forms
from home.models import NewIdeas, NewIdeasItems
from django_summernote.widgets import SummernoteWidget

class NewIdeasForm(forms.ModelForm):
    class Meta:
        model = NewIdeas
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control',}),
            'description': SummernoteWidget(),
        }

class NewIdeasItemsForm(forms.ModelForm):
    class Meta:
        model = NewIdeasItems
        fields = '__all__'
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class':'form-control', 'accept':'image/*',}),
            'title': forms.TextInput(attrs={'class':'form-control',}),
            'link': forms.URLInput(attrs={'class':'form-control',}),
        }