from django.contrib.admin.options import forms
from django.shortcuts import redirect, render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from users.forms import email
from . import forms

def home_view(request):
    return render(request, "index.html")

@login_required
def customerView(request):
    return render(request, "index.html")

@login_required
def courierView(request):
    return render(request, "index.html")

def register_page(request):
    form = forms.SignUpForm()
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email').lower()

            user = form.save(commit=False)
            user.username = email
            user.save()

            login(request, user)
            return redirect('home')
        else:
            return redirect('register')
    context = {'form': form}
    return render(request, "auth/register.html", context )
