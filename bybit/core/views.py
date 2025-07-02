from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import logging

logger = logging.getLogger(__name__)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Changed from 'email' to match form
        password = request.POST.get('password')
        logger.debug(f"Login attempt with username (email): {username}, password: {'*' * len(password) if password else None}")
        if not username:
            logger.error("No username provided in login attempt")
            messages.error(request, 'Email is required.')
            return render(request, 'login.html')
        if not password:
            logger.error("No password provided in login attempt")
            messages.error(request, 'Password is required.')
            return render(request, 'login.html')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            logger.debug(f"User {username} logged in successfully")
            return redirect(reverse('dashboard'))
        else:
            logger.debug(f"Authentication failed for {username}")
            messages.error(request, 'Invalid email or password.')
            return render(request, 'login.html')
    return render(request, 'login.html')

@csrf_exempt
def login_redirect_view(request):
    if request.method == 'POST':
        return JsonResponse({'redirect': reverse('login')})
    return JsonResponse({'error': 'Invalid request'}, status=400)

@login_required
def dashboard_view(request):
    logger.debug(f"Rendering dashboard for user: {request.user.email}, authenticated: {request.user.is_authenticated}")
    return render(request, 'dashboard.html', {'user': request.user})

@login_required
def logout_view(request):
    if request.method == 'POST':
        logger.debug(f"Logging out user: {request.user.email}")
        logout(request)
        return redirect(reverse('login'))
    return redirect(reverse('login'))