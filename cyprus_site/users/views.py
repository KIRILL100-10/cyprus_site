from django.contrib import messages
from django.contrib.auth import logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import RegisterForm, UserLoginForm, ProfileForm, UserPasswordChangeForm
from .mixins import ProfileMixin


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


class UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name = 'users/password_change.html'
    success_message = 'Password Change Successful!'
    success_url = reverse_lazy('password_change_done')


class UserPasswordChangeDoneView(LoginRequiredMixin, PasswordChangeDoneView):
    template_name = 'users/password_change_done.html'

