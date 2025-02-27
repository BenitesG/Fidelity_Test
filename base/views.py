from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm, LoginForm, CustomUser
from django.contrib import messages

# Home redirect
@login_required
def home(request):
    return render(request, "home.html", {})

# View for register / Register auth
def registerView(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if CustomUser.objects.filter(email=email).exists():
                messages.error(request, "Este email já está em uso.")
                return render(request, "registration/signup.html", {"form": form})
            
            form.save()

            return redirect("base:login") 

    return render(request, "registration/signup.html", {"form": form})

# Login auth
def loginView(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('base:home')
            else:
                try:
                    user = CustomUser.objects.get(email=email)
                    messages.error(request, 'E-mail ou senha inválidos')
                except CustomUser.DoesNotExist:
                    messages.error(request, 'E-mail inexistente')

    return render(request, 'registration/login.html', {'form': form})

def logoutView(request):
    logout(request)
    return redirect('base:login')  