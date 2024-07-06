from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.conf import settings
from django.contrib.auth.forms import User


        
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(help_text='A valid email address, please.', required=True)
    

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
class LoginForm(AuthenticationForm):
    def _init_(self, *args, **kwargs):
        super(LoginForm, self)._init_(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs ={'class': 'form-control', 'placeholder': 'Username or Email'}),
        label = 'Username or Email'
    )
    password = forms.CharField(widget=forms.PasswordInput(
        attrs ={'class': 'form-control', 'placeholder':'password'}))