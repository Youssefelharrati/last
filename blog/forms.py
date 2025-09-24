from django.forms import ModelForm
from .models import Post, Comment
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
 
class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['author', 'title', 'text']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class':'editable medium-editor-texterea postcontent'})
        }

class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['author', 'text']

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class':'editable medium-editor-texterea'})
        }

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    