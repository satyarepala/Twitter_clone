from django import forms
from .models import Post,Hashtag


class PostForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'your-css-class', 'rows': 5, 'cols': 40}),
                              max_length=100)
    hashtags = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'your-css-class'}))

    class Meta:
        model = Post
        fields = ['hashtags','message']