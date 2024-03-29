from django import forms
from .models import StaffMember, Visit, TempVisitNameMapping, Centre
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms.extras.widgets import SelectDateWidget


class NewStaffForm(forms.ModelForm):
    class Meta:
        model = StaffMember
        exclude = ("user_mapping",)


class BaseUserForm(forms.Form):
    user = forms.CharField(max_length=30)
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password",
                               widget=forms.PasswordInput,
                               max_length=80)
    password_repeat = forms.CharField(label="Repeat password",
                                      widget=forms.PasswordInput, max_length=80)

    def clean(self):
        cleaned_data = super(BaseUserForm, self).clean()
        if cleaned_data.get("password") != cleaned_data.get("password_repeat"):
            raise ValidationError("Passwords do not match",
                                  code="password_match")

class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = ("gender", "journey_stage", "visit_site", "nature_of_visit",
                  "cancer_site", "seen_by", "type", "activities")

class TempVisitNameMappingForm(forms.ModelForm):
    class Meta:
        model = TempVisitNameMapping
        fields = ("visitor_name",)


class ExportForm(forms.Form):
    startdate = forms.DateField(widget=SelectDateWidget)
    enddate = forms.DateField(widget=SelectDateWidget)
    center = forms.ModelChoiceField(queryset=Centre.objects)


