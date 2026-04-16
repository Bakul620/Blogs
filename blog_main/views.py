from django.shortcuts import render

from about.models import About, SocialLink
from blogs.models import Blog

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