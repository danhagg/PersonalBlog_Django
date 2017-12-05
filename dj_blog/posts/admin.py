from django.contrib import admin

from .models import Post


# ModelAdmin refers to Post model
# Need to set the Model itself
# we can play with the admin options here and check them in localhost:8000/admin
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'updated', 'timestamp']
    list_display_links = ['updated']
    list_editable = ['title']
    list_filter = ['updated', 'timestamp']
    search_fields = ['title', 'content']

    class Meta:
        model = Post


# Bring it in to admin.site.register
# We have now connected Post model with PostModelAdmin
admin.site.register(Post, PostModelAdmin)
