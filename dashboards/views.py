from django.shortcuts import render
from blogs.models import Blog, Categories
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def dashboard(request):
    context = {
        'category_count': Categories.objects.count(),
        'post_count': Blog.objects.count(),
    }
    return render(request, 'dashboard/dashboard.html', context)

def categories(request):
    return render(request, 'dashboard/categories.html')

def posts(request):
    posts = Blog.objects.all()
    context={
        'posts': posts,
    }
    return render(request, 'dashboard/posts.html', context)