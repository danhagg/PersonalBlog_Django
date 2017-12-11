from django import forms

from .models import Post

from markdownx.fields import MarkdownxFormField


# does this go into PostForm
class MyForm(forms.Form):
    myfield = MarkdownxFormField()


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "image", "draft", "publish"]
