from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from .models import Students
from django import forms
from django.contrib.auth import password_validation


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label="username", widget=forms.TextInput(attrs={"class":"form-control form-control-user","type":"text",
        "id":"exampleUserName","placeholder":"Username", "name":"username"}))
    first_name = forms.CharField(label="first_name", widget=forms.TextInput(attrs={"class":"form-control form-control-user","type":"text",
        "id":"exampleFirstName","placeholder":"First Name", "name":"first_name"}))
    last_name = forms.CharField(label="last_name", widget=forms.TextInput(attrs={"class":"form-control form-control-user", "type":"text", "id":"exampleLastName",
        "placeholder":"Last Name", "name":"last_name"}))
    mat_number = forms.CharField(label="mat_number", widget=forms.TextInput(attrs={"class":"form-control form-control-user","type":"text",
        "id":"exampleMatNumber","placeholder":"Mat Number", "name":"matnumber"}))
    email = forms.EmailField(label="email", widget=forms.EmailInput(attrs={"class":"form-control form-control-user", "type":"email", "id":"exampleInputEmail",
        "aria-describedby":"emailHelp", "placeholder":"Email Address", "name":"email"}))
    password1 = forms.CharField(help_text=password_validation.password_validators_help_text_html(),label="Password",
        widget=forms.PasswordInput(attrs={"class":"form-control form-control-user mb-2", "type":"password", "id":"examplePassword1",
        "placeholder":"Password", "name":"password"}))
    password2 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class":"form-control form-control-user", "type":"password", "id":"exampleRepeatPasswordInput",
        "placeholder":"Repeat Password", "name":"password_repeat"}))
    
    class Meta:
        model = Students
        fields = ('username','first_name','last_name','mat_number','email','password1','password2')


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label="username", widget=forms.EmailInput(attrs={"class":"form-control form-control-user", "type":"text", "id":"exampleInputUsername",
        "aria-describedby":"usernameHelp", "placeholder":"Enter Username", "name":"username"}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class":"form-control form-control-user", "type":"password", "id":"exampleInputPassword",
        "placeholder":"Password", "name":"password"}))
    
class UpdateUser(UserChangeForm):
    username = forms.CharField(label="username", widget=forms.TextInput(attrs={"class":"form-control", "type":"text", "id":"username"
        ,"placeholder":"{{ request.user.username }}","name":"username"}))
    first_name = forms.CharField(label="first_name", widget=forms.TextInput(attrs={"class":"form-control" ,"type":"text" ,"id":"first_name"
        ,"placeholder":"{{ request.user.last_name }}" ,"name":"last_name"}))
    last_name = forms.CharField(label="last_name", widget=forms.TextInput(attrs={"class":"form-control" ,"type":"text" ,"id":"last_name"
        ,"placeholder":"{{ request.user.last_name }}" ,"name":"last_name"}))
    email = forms.EmailField(label="email", widget=forms.EmailInput(attrs={"class":"form-control", "type":"email", "id":"email",
        "placeholder":"{{ request.user.email }}", "name":"email"}))
    mat_number = forms.CharField(label="last_name", error_messages={'unique': 'A user with that MatNO already exists.'},widget=forms.TextInput(attrs={"class":"form-control" ,"type":"text" ,"id":"mat_number"
        ,"placeholder":"{{ request.user.mat_number }}" ,"name":"mat_number"}))
    image = forms.ImageField(widget=forms.FileInput(attrs={"placeholder":"{{ request.user.image.url }}", "class":"form-control"}))
    bio = forms.CharField(label="Bio", widget=forms.Textarea(attrs={"class":"form-control","row":4,"type":"text" ,"id":"bio"
        ,"placeholder":"{{ request.user.bio }}" ,"name":"bio"}))
    
    class Meta:
        model = Students
        fields = ['username','first_name','last_name','email','mat_number','image','bio']

class ChangePass(PasswordChangeForm):
    old_password = forms.CharField(
        label="Old password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", "class":"form-control form-control-user", "type":"password", "id":"old_password",
        "placeholder":"old_password", "name":"old_password"}
        ),
    )
    new_password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class":"form-control form-control-user mb-3", "type":"password", "id":"new_password1",
        "placeholder":"new_password1", "name":"new_password1"}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label="New password confirmation",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class":"form-control form-control-user", "type":"password", "id":"new_password2",
        "placeholder":"new_password2", "name":"new_password2"}),
    )