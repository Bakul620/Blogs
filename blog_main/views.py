from django.shortcuts import redirect, render

from about.models import About, SocialLink
from .form import UserRegisterForm
from blogs.models import Blog
from django.contrib.auth.forms import AuthenticationForm

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
    form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request,'login.html', context)
