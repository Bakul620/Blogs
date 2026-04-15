from django.shortcuts import render

from blogs.models import Blog, Categories
def home(request):
    featured_posts = Blog.objects.filter(Is_featured=True,Status="Published").order_by('-Created_at')
    posts = Blog.objects.filter(Is_featured=False, Status="Published").order_by('-Created_at')
    context = {
        'featured_posts': featured_posts,
        'posts': posts,
    }
    return render(request,'home.html', context)