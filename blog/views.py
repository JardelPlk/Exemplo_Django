from django.shortcuts import render
from .models import Post

#Regra de negócio

def post_list(request):
    return render(request, 'blog/post_list.html', {})
