from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SignupForm
from django.contrib.auth import logout

from django.contrib import messages
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    PasswordChangeView,
    PasswordChangeDoneView,
)

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })
def home(request):

    return render(request, 'core/home.html', {})

    password_reset_view = PasswordResetView.as_view(
        template_name='registration/password_reset.html')


password_reset_done_view = PasswordResetDoneView.as_view(
    template_name='registration/password_reset_done.html')
password_reset_confirm_view = PasswordResetConfirmView.as_view(
    template_name='registration/password_reset_confirm.html')
password_reset_complete_view = PasswordResetCompleteView.as_view(
    template_name='registration/password_reset_complete.html')
password_change_view = PasswordChangeView.as_view(
    template_name='registration/password_change.html')
password_change_done_view = PasswordChangeDoneView.as_view(
    template_name='registration/password_change_done.html')
def logout_view(request):
    if request.user.is_authenticated:
        
        messages.success(request, 'You have been successfully logged out.')
        logout(request)
        return render(request, 'core/logout_confirmation.html')
    else:
        messages.info(request, 'You are not logged in.')
        return redirect('home')  

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })