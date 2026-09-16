from urllib import request

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

from myblog.models import Post
from django.contrib.auth.decorators import login_required




# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'myblog/index.html', {'posts': posts})




def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog_list')
    else:
        
        form = UserCreationForm()
    return render(request, 'myblog/signup.html', {'form': form})    


@login_required
def create_blog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = Post.objects.create(title=title, content=content, user=request.user)
        return redirect('blog_list')  # Redirect to the index page after creating the blog

    else:
        # Render the blog creation form
        return render(request, 'myblog/create_blog.html')



@login_required
def blog_list(request):
    posts = Post.objects.all()
    return render(request, 'myblog/blog_list.html', {'posts': posts})    

@login_required
def blog_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'myblog/detail.html', {'post': post})

@login_required
def edit_blog(request, post_id):
    post = Post.objects.get(id=post_id)
    if post.user != request.user:
        return HttpResponse("You are not authorized to edit this blog.", status=403)
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('blog_list')  # Redirect to the index page after editing the blog
    else:
        # Render the blog editing form with the existing post data
        return render(request, 'myblog/edit_blog.html', {'post': post})


@login_required
def delete_blog(request, post_id):
    post = Post.objects.get(id=post_id)
    if post.user != request.user:
        return HttpResponse("You are not authorized to delete this blog.", status=403)
    if request.method == 'POST':
        post.delete()
        return redirect('blog_list')  # Redirect to the index page after deleting the blog
  
        # Render a confirmation page before deleting the blog
    return render(request, 'myblog/delete_blog.html', {'post': post})    


def search_blogs(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(title__icontains=query) | Post.objects.filter(content__icontains=query)
    else:
        posts = Post.objects.all()
    return render(request, 'myblog/blog_list.html', {'posts': posts})