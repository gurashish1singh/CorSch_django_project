from django.shortcuts import render, redirect
from django.contrib import messages
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
            messages.success(request,f'Account created for {username}!')

            return redirect('blog-home')
    else:
    # Instatiating an empty form
        form = UserRegisterForm()

    
    context = {
        'form':form,
    }
    template_name = 'users/register.html'
    return render(request,template_name,context)