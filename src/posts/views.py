from django.http import HttpResponse
from django.shortcuts import render

# We will factor in functions for each CRUD component
# CREATE -- POST
# RETRIEVE -- GET -- List / Search
# UPDATE PUT/PATCH -- Edit
# DELETE --  DELETE -- Delete


def post_create(request):  # CREATE
    return HttpResponse('<h1>Create</h1>')


def post_detail(request):  # RETRIEVE
    context = {"title": "Detail"}
    return render(request, 'index.html', context)


def post_list(request):  # list items
    context = {"title": "List"}
    return render(request, 'index.html', context)


def post_update(request):  # UPDATE
    return HttpResponse('<h1>Update</h1>')


def post_delete(request):  # DELETE
    return HttpResponse('<h1>Delete</h1>')
