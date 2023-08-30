from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from .forms import ChangeUsernameForm, ChangeEmailForm, ChangeMobileNumberForm

@login_required()
def change_username(request):
    if request.method == 'POST':
        form = ChangeUsernameForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Username changed successfully.')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the errors below.')

    else:
        form = ChangeUsernameForm(instance=request.user)

    return render(request, 'django_setting/change_username.html', {'form': form})

@login_required()
def change_email(request):
    if request.method == 'POST':
        form = ChangeEmailForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Email changed successfully.')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ChangeEmailForm(instance=request.user)
    return render(request, 'django_setting/change_email.html', {'form': form})

@login_required()
def change_mobile_number(request):
    if request.method == 'POST':
        form = ChangeMobileNumberForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mobile number changed successfully.')
            print('Mobile number changed successfully.')
            return redirect('profile')
        else:
            print(form.errors)
            print('Mobile number failed to update')
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ChangeMobileNumberForm(instance=request.user)
    return render(request, 'django_setting/change_mobile_number.html', {'form': form})

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'django_setting/change_password.html'  # Replace with your template

    def form_valid(self, form):
        print("Password changed successfully.")
        messages.success(self.request, 'Password changed successfully.')  # Add your success message here
        return super().form_valid(form)

@login_required()
def setting(request):
    return render(request, 'django_setting/setting.html')
