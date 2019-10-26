from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm

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
    context = {

    }
    template_name='users/profile.html'
    return render(request, template_name, context)