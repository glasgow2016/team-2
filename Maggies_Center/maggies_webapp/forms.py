from django import forms
from .models import StaffMember
from django.contrib.auth.models import User, Visit


class NewStaffForm(forms.ModelForm):
    class Meta:
        model = StaffMember
        exclude = ("user_mapping",)


class BaseUserForm(forms.Form):
    user = forms.CharField(max_length=30)
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password", widget=forms.PasswordInput, max_length=80)
    password_repeat = forms.CharField(label="Repeat password", widget=forms.PasswordInput, max_length=80)

class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
