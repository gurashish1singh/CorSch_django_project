from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# # Types of messages
# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error

# Create your views here.
def register(request):
    # If method is POST 
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        # Saving the form and cleeaning the form after submission
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Your account has been created. Please Login!!')
            return redirect('login')
    else:
    # Instatiating an empty form
        form = UserRegisterForm()

    
    context = {
        'form':form,
    }
    template_name = 'users/register.html'
    return render(request,template_name,context)

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    template_name='users/profile.html'
    return render(request, template_name, context)