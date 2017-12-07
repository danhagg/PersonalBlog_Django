from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Post


def post_create(request):  # CREATE
    return HttpResponse('<h1>Create</h1>')


def post_detail(request, id):  # RETRIEVE
    instance = get_object_or_404(Post, id=id)
    context = {"title": instance.title, "instance": instance}
    return render(request, 'post_detail.html', context)


def post_list(request):  # list items
    queryset = Post.objects.all()
    context = {"object_list": queryset, "title": "List"}
    return render(request, 'index.html', context)


def post_update(request):  # UPDATE
    return HttpResponse('<h1>Update</h1>')


def post_delete(request):  # DELETE
    return HttpResponse('<h1>Delete</h1>')
