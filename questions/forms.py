from django import forms  
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User
import re

class SignupForm(UserCreationForm):  
    password1 = forms.CharField(
        label="كلمة المرور",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    password2 = forms.CharField(
        label="تكرار كلمة المرور",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=None
    )
    username = forms.CharField(
        label="اسم المستخدم",
        widget=forms.TextInput,
        help_text=None
    )
    first_name = forms.CharField(
        label="الاسم",
        widget=forms.TextInput,
    )
    last_name = forms.CharField(
        label="الكنية",
        widget=forms.TextInput,
    )
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
            self.add_error(None, u' مستخدم من قبل"%s" اسم المستخدم*' % username)
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 != password2:
            self.add_error(None, "كلمات المرور غير متطابقة*")
        else:
            if len(password2) < 10:
                self.add_error(None,"كلمة المرور يجب ان تكون اكثر من 10 خانات*")
        return password2
    
    class Meta:  
        model = User
        fields = ('username','first_name','last_name')

    def __init__(self, *args, **kwargs):
        super(SignupForm,self).__init__(*args, **kwargs)

