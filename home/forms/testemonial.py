from django import forms
from home.models import Testemonial, TestemonialsItems
from django_summernote.widgets import SummernoteWidget

class TeatemonialForm(forms.ModelForm):
    class Meta:
        model = Testemonial
        fields = '__all__'
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class':'form-control', 'accept': 'image/*',}),
            'title': forms.TextInput(attrs={'class':'form-control',}),
            'link': forms.URLInput(attrs={'class':'form-control',}),
        }

class TestemonialItemsForm(forms.ModelForm):
    class Meta:
        model = TestemonialsItems
        fields = '__all__'
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class':'form-control', 'accept':'image/*',}),
            'name': forms.TextInput(attrs={'class':'form-control',}),
            'call': forms.TextInput(attrs={'class':'form-control',}),
            'link': forms.URLInput(attrs={'class':'form-control',}),
            'comment': SummernoteWidget(),
        }