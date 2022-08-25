from django.shortcuts import render, get_object_or_404
from .models import Post


# Create your views here.


def all_news(request):
    post = Post.objects.order_by('dateCreation')
    return render(request, 'news.html', context={'news': post})


def one_new(request, id:int):
    new = get_object_or_404(Post, id=id)
    return render(request, 'one_new.html', {'new': new})


