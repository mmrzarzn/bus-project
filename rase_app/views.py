from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .models import User
from django.utils.crypto import get_random_string
from django.http import Http404, HttpRequest
from django.contrib.auth import login, logout
from .forms import RegisterForm, LoginForm, ForgetPasswordForm, ResetPasswordForm
class HomeView(TemplateView):
    template_name = 'rase_app/home.html'


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {
            'register_form': register_form
        }

        return render(request, 'rase_app/Signup.html', context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_email = register_form.cleaned_data.get('email')
            user_name = register_form.cleaned_data.get('name')
            user_password = register_form.cleaned_data.get('password')
            user: bool = User.objects.filter(email__iexact=user_email).exists()
            if user:
                register_form.add_error('email', 'The entered email is duplicate')
            else:
                new_user = User(
                    email=user_email,
                    # name=user_name,
                    is_active=False,
                    username=user_email
                    )
                new_user.set_password(user_password)
                new_user.save()
                return redirect(reverse('login_page'))

        context = {
            'register_form': register_form
        }

        return render(request, 'rase_app/Signup.html', context)


# class ActivateAccountView(View):
#     def get(self, request, email_active_code):
#         user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()
#         if user is not None:
#             if not user.is_active:
#                 user.is_active = True
#                 user.email_active_code = get_random_string(72)
#                 user.save()
#                 # todo: show success message to user
#                 return redirect(reverse('login_page'))
#             else:
#                 # todo: show your account was activated message to user
#                 pass
#
#         raise Http404


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }

        return render(request, 'rase_app/SignupLogin.html', context)

    def post(self, request: HttpRequest):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_pass = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                if not user.is_active:
                    login_form.add_error('email', 'Your account has not been activated')
                else:
                    is_password_correct = user.check_password(user_pass)
                    if is_password_correct:
                        login(request, user)
                        return redirect(reverse('time_page'))
                    else:
                        login_form.add_error('email', 'The password is wrong')
            else:
                login_form.add_error('email', 'A user with the entered profile was not found')

        context = {
            'login_form': login_form
        }

        return redirect(reverse('time_page'), context)

#
# class ForgetPasswordView(View):
#     def get(self, request: HttpRequest):
#         forget_pass_form = ForgetPasswordForm()
#         context = {'forget_pass_form': forget_pass_form}
#         return render(request, 'rase_app/forgot_password.html', context)
#
#     def post(self, request: HttpRequest):
#         forget_pass_form = ForgetPasswordForm(request.POST)
#         if forget_pass_form.is_valid():
#             user_email = forget_pass_form.cleaned_data.get('email')
#             user: User = User.objects.filter(email__iexact=user_email).first()
#             if user is not None:
#                 send_email('Password recovery', user.email, {'user': user}, 'emails/forgot_password.html')
#             return redirect(reverse('home_page'))
#
#         context = {'forget_pass_form': forget_pass_form}
#         return render(request, 'rase_app/forgot_password.html', context)
#
#
# class ResetPasswordView(View):
#     def get(self, request: HttpRequest, active_code):
#         user: User = User.objects.filter(email_active_code__iexact=active_code).first()
#         if user is None:
#             return redirect(reverse('login_page'))
#
#         reset_pass_form = ResetPasswordForm()
#
#         context = {
#             'reset_pass_form': reset_pass_form,
#             'user': user
#         }
#         return render(request, 'rase_app/reset_password.html', context)
#
#     def post(self, request: HttpRequest, active_code):
#         reset_pass_form = ResetPasswordForm(request.POST)
#         user: User = User.objects.filter(email_active_code__iexact=active_code).first()
#         if reset_pass_form.is_valid():
#             if user is None:
#                 return redirect(reverse('login_page'))
#             user_new_pass = reset_pass_form.cleaned_data.get('password')
#             user.set_password(user_new_pass)
#             user.email_active_code = get_random_string(72)
#             user.is_active = True
#             user.save()
#             return redirect(reverse('login_page'))
#
#         context = {
#             'reset_pass_form': reset_pass_form,
#             'user': user
#         }
#
#         return render(request, 'rase_app/reset_password.html', context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('login_page'))
