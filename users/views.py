from django.shortcuts import render, redirect
from django.contrib import messages  #messages such as mesages.debug, messages.info, messages.success etc
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()    #sasve the user in the system
            username = form.cleaned_data.get('username') # cleaned_data is dictionary
            messages.success(request, f'계정이 성공적으로 만들어졌습니다! 지금부터 로그인이 가능합니다!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required    #decorator that adds functinality to function that user must be logged in to view this page
def profile(request):
    return render(request, 'users/profile.html')


