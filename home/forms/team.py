from home.models import Team
from django import forms
from django_summernote.widgets import SummernoteWidget

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'
        widgets = {
            'image' : forms.ClearableFileInput(attrs={'class':'form-control', 'accept':'image/*',}),
            'title' : forms.TextInput(attrs={'class':'form-control',}),
            'description' : SummernoteWidget(),
            'short' : forms.TextInput(attrs={'class':'form-control',}),
            'link' : forms.URLInput(attrs={'class':'form-control',})
        }