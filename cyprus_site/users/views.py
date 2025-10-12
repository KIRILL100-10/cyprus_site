from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, FormView, TemplateView
from django.urls import reverse_lazy

from .forms import RegisterForm, UserLoginForm, ProfileForm, UserPasswordChangeForm, UserPasswordResetForm, \
    UserPasswordResetConfirmForm, FeedbackForm
from .mixins import ProfileMixin

import os


class RegisterView(SuccessMessageMixin, CreateView):
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_message = 'Registration Successful!'
    success_url = reverse_lazy('login')


class UserLoginView(SuccessMessageMixin, LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'
    success_message = 'Login Successful!'


class UserLogoutView(SuccessMessageMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, 'You have been logged out.')
        return redirect('home')


class Profile(LoginRequiredMixin, ProfileMixin, DetailView):
    template_name = 'users/profile.html'
    context_object_name = 'profile'


class ProfileUpdate(LoginRequiredMixin, ProfileMixin, SuccessMessageMixin, UpdateView):
    form_class = ProfileForm
    template_name = 'users/profile_update.html'
    success_message = 'Profile Update Successful!'
    success_url = reverse_lazy('home')


class ProfileDelete(LoginRequiredMixin, ProfileMixin, SuccessMessageMixin, DeleteView):
    template_name = 'users/profile_delete.html'
    success_message = 'Profile Delete Successful!'
    success_url = reverse_lazy('home')


class UserPasswordChangeView(LoginRequiredMixin, SuccessMessageMixin, PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name = 'users/password_change.html'
    success_message = 'Password Change Successful!'
    success_url = reverse_lazy('users:password_change_done')


class UserPasswordChangeDoneView(LoginRequiredMixin, PasswordChangeDoneView):
    template_name = 'users/password_change_done.html'


class UserPasswordResetView(SuccessMessageMixin, PasswordResetView):
    form_class = UserPasswordResetForm
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    success_message = 'Password Reset Successful!'
    success_url = reverse_lazy('users:password_reset_done')


class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'


class UserPasswordResetConfirmView(SuccessMessageMixin, PasswordResetConfirmView):
    form_class = UserPasswordResetConfirmForm
    template_name = 'users/password_reset_confirm.html'
    success_message = 'Password Reset Confirm Successful!'
    success_url = reverse_lazy('users:password_reset_complete')


class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'users/password_reset_complete.html'


class ContactView(LoginRequiredMixin, SuccessMessageMixin, FormView):
    form_class = FeedbackForm
    template_name = 'users/contact.html'
    success_message = 'Thank You for your feedback.'
    success_url = reverse_lazy('users:contact_done')

    def form_valid(self, form):
        print(form.cleaned_data)
        email = form.cleaned_data.get('email', 'No email')
        subject = form.cleaned_data.get('subject', 'No subject')
        message = form.cleaned_data.get('message', 'No message')

        print(send_mail(subject=subject, message=message, from_email=email, recipient_list=[os.getenv('EMAIL_CONTACT')], fail_silently=False))
        return super().form_valid(form)


class ContactDoneView(LoginRequiredMixin, TemplateView):
    template_name = 'users/contact_done.html'
