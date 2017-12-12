from django import forms

from .models import Post

from markdownx.fields import MarkdownxFormField


class PostForm(forms.ModelForm):
    publish = forms.DateField(widget=forms.SelectDateWidget)
    content = MarkdownxFormField()

    class Meta:
        model = Post
        fields = ["title", "content", "image", "draft", "publish"]
