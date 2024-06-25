from django import forms
from home.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class':'contactus','placeholder':'Nome','type':'type',}),
            'email': forms.EmailInput(attrs={'class':'contactus','placeholder':'Email','type':'type',}),
            'phone': forms.TextInput(attrs={'class':'contactus','placeholder':'Fone','type':'type',}),
            'message': forms.Textarea(attrs={'class':'contactus1','placeholder':'Mensagem','type':'type',}),
        }