from django import forms
from .models import Subscription,Comments,Blog,Contacts

class Subform(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['email', ]


class Comentsform(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['full_name','email','phone','message' ]
        exclude = ['blog', ]


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ["full_name", "email", "phone", "massage"]