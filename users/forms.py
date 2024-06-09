from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

from catalog.forms import StileFormMixin
from users.models import User


class UserRegisterForm(StileFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "password1", "password2")


class ResetPasswordForm(forms.Form):
    email = forms.EmailField(label="Email")

    def clean_email(self):
        email = self.cleaned_data["email"]
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "Пользователь с таким адресом электронной почты не найден"
            )
        return email
