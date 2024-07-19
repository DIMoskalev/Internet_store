import secrets

from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from config import settings
from users.forms import RegisterForm, UserProfileForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email_confirm/{token}/'
        send_mail(
            'Confirm email',
            f'Click the link to confirm your email: {url}',
            settings.EMAIL_HOST_USER,
            [user.email],
        )

        return super().form_valid(form)


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def email_confirm(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.token = None
    user.save()
    return redirect(reverse('users:login'))


def pass_recovery(request):
    if request.method == 'GET':
        return render(request, 'users/pass_recovery.html')
    if request.method == 'POST':
        email = request.POST.get('email')
        user = get_object_or_404(User, email=email)
        password = User.objects.make_random_password(length=10)
        user.set_password(password)
        user.save()
        send_mail(
            'Password recovery',
            f'Your new password: {password}',
            settings.EMAIL_HOST_USER,
            [user.email],
        )
        return redirect(reverse('users:login'))
