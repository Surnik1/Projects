from django import forms
from .models import User, Article, Comment


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["name", "psw"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Enter your name"}),
            "psw": forms.PasswordInput(attrs={"placeholder": "Enter your password"}),
        }


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["head", "text"]
        widgets = {
            "head": forms.TextInput(attrs={"placeholder": "Title"}),
            "text": forms.Textarea(attrs={"placeholder": "Text"}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
        widgets = {
            "text": forms.Textarea(attrs={"placeholder": "Your comment..."}),
        }
