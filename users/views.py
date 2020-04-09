from django.shortcuts import render, redirect
from django.contrib import messages  #messages such as mesages.debug, messages.info, messages.success etc
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()    #sasve the user in the system
            username = form.cleaned_data.get('username') # cleaned_data is dictionary
            messages.success(request, f'{username}으로 회원가입 되셨습니다!')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


