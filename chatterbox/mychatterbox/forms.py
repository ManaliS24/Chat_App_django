from django import forms
from django.forms import ModelForm
from .models import ChatMessage, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ChatMessageForm(ModelForm):
    body= forms.CharField(widget=forms.Textarea(attrs={"class": "forms", "rows": 2, "placeholder": "Type Message Here."}))
    class Meta:
        model =ChatMessage
        fields=["body"]


class UserForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    username= forms.CharField()

    class Meta:
        model =User
        fields=["first_name","last_name","username"]