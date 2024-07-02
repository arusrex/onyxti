from home.models import BlogItems
from django import forms
from django_summernote.widgets import SummernoteWidget

class BlogItemsForm(forms.ModelForm):
    class Meta:
        model = BlogItems
        fields = '__all__'
        widgets = {
            'slug': forms.TextInput(attrs={'class':'form-control', 'readonly':'true'},),
            'title': forms.TextInput(attrs={'class':'form-control'},),
            'image': forms.ClearableFileInput(attrs={'class':'form-control'},),
            'short': forms.TextInput(attrs={'class':'form-control'},),
            'description': SummernoteWidget(),
            'buttom_name': forms.TextInput(attrs={'class':'form-control'},),
            'link': forms.URLInput(attrs={'class':'form-control'},),
            'created_at': forms.DateTimeInput(attrs={'class':'form-control'},),
            'updated_at': forms.DateTimeInput(attrs={'class':'form-control'},),
        }