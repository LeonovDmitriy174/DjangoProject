from django import forms

from blog.models import Blog


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        exclude = ("slug", "view_count", "created_at", "is_published")
