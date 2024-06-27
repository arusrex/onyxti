from site_setup.models import SiteSetup, MenuLinks
from django import forms
from django_summernote.widgets import SummernoteWidget
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User


class SiteSetupForm(forms.ModelForm):
    class Meta:
        model = SiteSetup
        fields = '__all__'
        widgets = {
            'show_logo': forms.CheckboxInput(attrs={'class':'form-check-input',}),
            'show_menu': forms.CheckboxInput(attrs={'class':'form-check-input',}),
            'show_header': forms.CheckboxInput(attrs={'class':'form-check-input',}),
            'show_footer': forms.CheckboxInput(attrs={'class':'form-check-input',}),
            'show_search': forms.CheckboxInput(attrs={'class':'form-check-input',}),
            'show_carousel': forms.CheckboxInput(attrs={'class':'form-check-input',}),
            'show_team': forms.CheckboxInput(attrs={'class':'form-check-input',}),
            'show_services': forms.CheckboxInput(attrs={'class':'form-check-input',}),
            'show_new_ideas': forms.CheckboxInput(attrs={'class':'form-check-input',}),
            'show_testemonial': forms.CheckboxInput(attrs={'class':'form-check-input',}),
            'show_contact': forms.CheckboxInput(attrs={'class':'form-check-input',}),
            'show_newsletter': forms.CheckboxInput(attrs={'class':'form-check-input',}),
            'show_socials': forms.CheckboxInput(attrs={'class':'form-check-input',}),

            'site_name': forms.TextInput(attrs={'class':'form-control',}),
            'site_description': SummernoteWidget(),
            'contact_email': forms.EmailInput(attrs={'class':'form-control',}),
            'phone_number': forms.TextInput(attrs={'class':'form-control',}),

            'favicon': forms.ClearableFileInput(attrs={'class':'form-control', 'accept':'image/*',}),
            'logo': forms.ClearableFileInput(attrs={'class':'form-control', 'accept':'image/*',}),
            'logo2': forms.ClearableFileInput(attrs={'class':'form-control', 'accept':'image/*',}),

            'facebook': forms.URLInput(attrs={'class':'form-control',}),
            'instagram': forms.URLInput(attrs={'class':'form-control',}),
            'x_twitter': forms.URLInput(attrs={'class':'form-control',}),
            'youtube': forms.URLInput(attrs={'class':'form-control',}),
            'tiktok': forms.URLInput(attrs={'class':'form-control',}),
        }

class MenuLinksForm(forms.ModelForm):
    class Meta:
        model = MenuLinks
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control',}),
            'url': forms.URLInput(attrs={'class':'form-control',}),
        }

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

class EditUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_staff', 'is_superuser', 'is_active']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'},),
            'first_name':forms.TextInput(attrs={'class':'form-control'},),
            'last_name':forms.TextInput(attrs={'class':'form-control'},),
            'email':forms.EmailInput(attrs={'class':'form-control'},),
            'is_staff':forms.CheckboxInput(attrs={'class':'form-check-input'},),
            'is_superuser':forms.CheckboxInput(attrs={'class':'form-check-input'},),
            'is_active':forms.CheckboxInput(attrs={'class':'form-check-input'},),
        }

class PasswordEditForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']

    def __init__(self, *args, **kwargs):
        super(PasswordEditForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

