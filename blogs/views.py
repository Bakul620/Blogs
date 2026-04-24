from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from .models import Blog, Categories,Comment
from django.db.models import Q

def post_by_category(request, Category_id):
    category = get_object_or_404(Categories, pk=Category_id)
    posts = Blog.objects.filter(Category_id=Category_id, Status="Published").order_by('-Created_at')

    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'post_by_category.html', context)

def blog_detail(request, slug):
    single_blog = get_object_or_404(Blog, Slug=slug, Status="Published")
    if request.method == 'POST':
        comment = Comment()
        comment.Blog = single_blog
        comment.User = request.user
        comment.Comment_text = request.POST.get('comment')
        comment.save()
        return HttpResponseRedirect(request.path_info)

    comment=Comment.objects.filter(Blog=single_blog)
    context = {
        'single_blog': single_blog,
        'comments': comment,
    }
    return render(request, 'blog_detail.html', context)

def search(request):
    keyword = (request.GET.get('keyword') or '').strip()
    blogs = Blog.objects.none()

    if keyword:
        blogs = Blog.objects.filter(
            Q(Title__icontains=keyword) |
            Q(Description__icontains=keyword) |
            Q(Blog_body__icontains=keyword),
            Status="Published"
        )

    context = {
        'blogs': blogs,
        'keyword': keyword,
    }
    return render(request, 'search.html', context)