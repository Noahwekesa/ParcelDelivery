from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AttributesCustomerForm, ProfileUserForm
from django.urls import reverse
from django.contrib import messages
# Create your views here.
@login_required
def customerView(request):
    return redirect(reverse('customer:profile'))

@login_required(login_url="/register/?next=/customer/")
def profile_page(request):
    user_form = ProfileUserForm(instance=request.user)
    customer_form = AttributesCustomerForm(request.POST, request.FILES, instance=request.user.customer)
    if request.method == 'POST':
        user_form = ProfileUserForm(request.POST, instance=request.user)
        if user_form.is_valid() and customer_form.is_valid():
            user_form.save()
            customer_form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect(reverse('customer:profile'))
    else:
        user_form = ProfileUserForm(request.POST, instance=request.user)

    context = {"user_form": user_form, "customer_form": customer_form}
    return render(request, 'profile.html', context)
