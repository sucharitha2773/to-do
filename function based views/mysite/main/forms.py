from django import forms
from main.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =('content','text','image',)

       