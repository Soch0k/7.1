from django import forms
from  django.contrib.auth.forms import UserCreationForm, UserChangeForm
from  .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        Model = CustomUser
        fields = UserCreationForm.Meta.fields

class CustomUserChangeForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields