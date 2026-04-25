from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseForbidden
from .forms import AddUserForm, CategoryForm, EditUserForm, PostForm
from blogs.models import Blog, Categories
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


@login_required(login_url='login')
def dashboard(request):
    context = {
        'category_count': Categories.objects.count(),
        'post_count': Blog.objects.count(),
    }
    return render(request, 'dashboard/dashboard.html', context)

@login_required(login_url='login')
def categories(request):
    categories = Categories.objects.all().order_by('-Created_at')
    context = {
        'categories': categories,
    }
    return render(request, 'dashboard/categories.html', context)


@login_required(login_url='login')
def add_category(request):
    if request.method=='POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.Author = request.user
            category.save()
            return redirect('categories')
    form = CategoryForm()
    context={
        'form': form,
    }
    return render(request, 'dashboard/add_category.html', context)

@login_required(login_url='login')
def edit_category(request, pk):
    category = get_object_or_404(Categories, pk=pk)
    if category.Author != request.user and not request.user.is_staff and not request.user.is_superuser:
        return HttpResponseForbidden('You do not have permission to edit this category.')
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    
    form=CategoryForm(instance=category)
    context={
        'form': form,
        'category': category,
    }
    return render(request, 'dashboard/edit_category.html', context)

@login_required(login_url='login')
def delete_category(request, pk):
    category = get_object_or_404(Categories, pk=pk)
    if category.Author != request.user and not request.user.is_staff and not request.user.is_superuser:
        return HttpResponseForbidden('You do not have permission to delete this category.')
    category.delete()
    return redirect('categories')


def posts(request):
    posts = Blog.objects.all()
    context={
        'posts': posts,
    }
    return render(request, 'dashboard/posts.html', context)

@login_required(login_url='login')
def add_post(request):
    if request.method=='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post=form.save(commit=False) # temporarily save the form data to get the post object
            post.Author = request.user
            post.save()
            title = form.cleaned_data['Title']
            post.Slug = slugify(title) + '-' + str(post.id)
            post.save()
            return redirect('posts')
    form = PostForm()
    context={
        'form': form,
    }
    return render(request, 'dashboard/add_post.html', context)

@login_required(login_url='login')
def edit_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if post.Author != request.user and not request.user.is_staff and not request.user.is_superuser:
        return HttpResponseForbidden('You do not have permission to edit this post.')
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            title = form.cleaned_data['Title']
            post.Slug = slugify(title) + '-' + str(post.id)
            post.save()
            return redirect('posts')
    
    form=PostForm(instance=post)
    context={
        'form': form,
        'post': post,
    }
    return render(request, 'dashboard/edit_post.html', context)

@login_required(login_url='login')
def delete_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if post.Author != request.user and not request.user.is_staff and not request.user.is_superuser:
        return HttpResponseForbidden('You do not have permission to delete this post.')
    post.delete()
    return redirect('posts')


def users(request):
    users = User.objects.all()
    context={
        'users': users,
    }
    return render(request, 'dashboard/users.html', context)

def add_user(request):
    if request.method=='POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
        else:
            print(form.errors)
    form = AddUserForm()
    context={
        'form': form,
    }
    return render(request, 'dashboard/add_user.html',context)

def edit_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
        
    form = EditUserForm(instance=user)
    context={
        'form': form,
    }
    return render(request, 'dashboard/edit_user.html',context)

def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect('users')
    