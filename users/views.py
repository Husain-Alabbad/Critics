from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from .forms import UserRigesterForm, ProfileUpdateForm

# Create your views here.



def register(request):
    if request.method == 'POST':
        form = UserRigesterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'your account has been created {username}, Login and Enjoy')
            return redirect('login')
    else:
        form = UserRigesterForm()
    return render(request, 'users/register.html',{'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request,f'your Profile has been updated , Login and Enjoy')
            return redirect('profile')

    else:
       form = ProfileUpdateForm(instance=request.user.profile)

    context = {'form':form}
    return render(request, 'users/profile.html', context)
