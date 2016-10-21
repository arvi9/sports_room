from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class StudentCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=13, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'phone_number')

    def save(self, commit=True):
        user = super(StudentCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user._phone_number = self.cleaned_data['phone_number']
        if commit:
            user.save()
        return user
