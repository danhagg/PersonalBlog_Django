from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include

# will port only from posts/views
from .views import (
    post_list,
    post_create,
    post_detail,
    post_update,
    post_delete,
)

# we can make our urls linked to view functions
# lists is simply going to be the default posts url
urlpatterns = [
    url(r'^$', post_list, name='list'),
    url(r'^create/$', post_create),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
]
