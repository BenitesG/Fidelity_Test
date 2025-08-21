from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm, LoginForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm
from django.core.cache import cache

def get_client_ip(request):
    """Obtém o IP do cliente de forma confiável."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

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
            
            form.save()

            return redirect("base:login") 

    return render(request, "registration/signup.html", {"form": form})

# Login auth with cache attempt block
def loginView(request):
    # Client ip
    client_ip = get_client_ip(request)
    cache_key = f'login_attempts:{client_ip}'
    
    login_attempts = cache.get(cache_key, 0)
    LOGIN_ATTEMPT_LIMIT = 5

    if request.method == 'POST':
        if login_attempts >= LOGIN_ATTEMPT_LIMIT:
            messages.error(request, 'Você excedeu o número de tentativas de login. Por favor, tente novamente mais tarde.')
            return render(request, 'registration/login.html', {'form': LoginForm()})

        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            
            if user is not None:
                cache.delete(cache_key)
                login(request, user)
                return redirect('base:home')
            else:
                login_attempts += 1
                cache.set(cache_key, login_attempts, timeout=300) 
                
                messages.error(request, 'E-mail ou senha inválidos.')
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})

def logoutView(request):
    logout(request)
    return redirect('base:login')  