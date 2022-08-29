from django.shortcuts import render
from . models import Category, Post, Comment


def blog_index(request):
    categorys = Category.objects.all()
    posts = Post.objects.all().order_by('-created_on')
    comments = Comment.objects.all()
    context = {
        'categorys': categorys,
        'posts': posts,
        'comments': comments
    }
    return render(request, 'blog_index.html', context)


def blog_detail(request, pk):
    category = Category.objects.get(pk=pk)
    post = Post.objects.get(pk=pk)
    comment = Comment.objects.get(pk=pk)
    context = {
        'category': category,
        'post': post,
        'comment': comment
    }
    return render(request, 'blog_detail.html', context)
