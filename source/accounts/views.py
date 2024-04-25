from django.shortcuts import render, redirect
from accounts.forms import SignupForm
from django.contrib.auth import logout


# Регистрация пользователя
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('webapp:test_list_view')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


# Выйти
def custom_logout(request):
    logout(request)
    return redirect('webapp:index')

