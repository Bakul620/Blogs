from django.shortcuts import redirect, render

from about.models import About, SocialLink
from .form import UserRegisterForm
from blogs.models import Blog
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.models import User

def home(request):
    featured_posts = Blog.objects.filter(Is_featured=True,Status="Published").order_by('-Created_at')
    posts = Blog.objects.filter(Is_featured=False, Status="Published").order_by('-Created_at')
    # Fetch about data
    try:
        about = About.objects.get()
    except:
        about = None

    social_link = SocialLink.objects.all()
    context = {
        'featured_posts': featured_posts,
        'posts': posts,
        'about': about,
        'social_link': social_link,
    }
    return render(request,'home.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserRegisterForm()
    context = {
        'form': form
    }
    return render(request,'register.html', context)

def login(request):
    if request.method== 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
    else:
        form = AuthenticationForm()

    context = {
        'form': form
    }
    return render(request,'login.html', context)

def logout(request):
    auth.logout(request)
    return redirect('home')


