from django import forms
from accounts.models import Usuario

class RegisterUserForm(forms.ModelForm):

    class Meta:
        password = forms.CharField(widget=forms.PasswordInput())
        email = forms.CharField(widget=forms.EmailInput())
        model = Usuario
        fields = '__all__'

        widgets = {
            'password': forms.PasswordInput(),
            'email': forms.EmailInput(),
        }
