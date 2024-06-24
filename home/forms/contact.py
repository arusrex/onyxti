from django import forms
from home.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class':'contactus',}),
            'email': forms.EmailInput(attrs={'class':'contactus',}),
            'phone': forms.TextInput(attrs={'class':'contactus',}),
            'message': forms.Textarea(attrs={'class':'contactus1',}),
        }