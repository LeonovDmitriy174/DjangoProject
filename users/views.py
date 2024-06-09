import random
import secrets
import string

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm, ResetPasswordForm
from users.models import User

from django.core.mail import send_mail


class UserCreateView(LoginRequiredMixin, CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f"http://{host}/users/email-confirm/{token}/"
        send_mail(
            subject="Подтверждение почты",
            message=f"Привет! Для подтверждения почты перейдите по ссылке {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))


def reset_password(request):
    if request.method == "POST":
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            user = User.objects.get(email=email)
            characters = string.ascii_letters + string.digits
            characters_list = list(characters)
            random.shuffle(characters_list)
            password = "".join(characters_list[:10])
            user.set_password(password)
            user.save()
            send_mail(
                subject="Восстановление пароля",
                message=f"Здравствуйте, вы запрашивали обновление пароля. Ваш новый пароль: {password}",
                from_email=EMAIL_HOST_USER,
                recipient_list=[user.email],
            )
            return redirect("/users/login")
    else:
        form = ResetPasswordForm()
    return render(request, "users/reset_password.html", {"form": form})
