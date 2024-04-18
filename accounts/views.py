from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('profile')  # Assuming there's a URL named 'profile'
    else:
        form = UserCreationForm()
    return render(request, 'accounts/registration.html', {'form': form})

def profile(request):
    user = request.user
    return render(request, 'accounts/profile.html', {'user': user})