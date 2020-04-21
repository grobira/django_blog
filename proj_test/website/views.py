from django.shortcuts import render
from .models import Post, Contact


def hello_blog(request):
    list_post = Post.objects.filter(deleted=False)
    data = {'posts': list_post}
    return render(request, 'index.html', data)


def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post_detail.html', {'post': post})


def save_form(request):
    Contact.objects.create(
        name=request.POST['name'],
        email=request.POST['email'],
        message=request.POST['message'],
    )
    return hello_blog(request)