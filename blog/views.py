from django.shortcuts import render, get_object_or_404
from django.utils import timezone
#from django.http import Http404
from django.contrib.auth.models import User
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect




#Regra de negócio

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())
    users = User.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts, 'users': users})

def post_detail(request, pk):
    #try:
    #    post = Post.objects.get(pk=pk)
    #except Post.DoesNotExist:
    #    raise Http404('Post missing =/')#Caso a página não exista
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'blog/post_detail.html', {'post': post})

def author_perfil(request, pk):
    author = get_object_or_404(User, pk=pk)
    posts = Post.objects.filter(author=author)

    return render(request, 'blog/author_perfil.html', {'author': author, 'posts': posts})

def post_new(request):
     if request.method == "POST":
         form = PostForm(request.POST)
         if form.is_valid():
             post = form.save(commit=False)
             post.author = request.user
             post.published_date = timezone.now()
             post.save()
             return redirect('post_detail', pk=post.pk)
     else:
         form = PostForm()
     return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
     post = get_object_or_404(Post, pk=pk)
     if request.method == "POST":
         form = PostForm(request.POST, instance=post)
         if form.is_valid():
             post = form.save(commit=False)
             post.author = request.user
             post.published_date = timezone.now()
             post.save()
             return redirect('post_detail', pk=post.pk)
     else:
         form = PostForm(instance=post)
     return render(request, 'blog/post_edit.html', {'form': form})
