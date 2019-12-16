from django import forms

from .models import Post,Answers

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('question',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Answers
        fields = ('text',)