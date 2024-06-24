from django import forms
from home.models import NewsLetter

class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = '__all__'
        widgets = {
            'email': forms.TextInput(attrs={'class':'enter',}),
        }