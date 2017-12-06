from django.conf.urls import url
from django.contrib import admin

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
    url(r'^$', post_list),
    url(r'^create/$', post_create),
    url(r'^detail/$', post_detail),
    url(r'^update/$', post_update),
    url(r'^delete/$', post_delete),
]
