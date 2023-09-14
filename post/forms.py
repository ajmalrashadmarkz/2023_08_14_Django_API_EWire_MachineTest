from django import forms
from .models import Post
from .models import Tag

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"