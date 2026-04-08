from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Comment, Article
from .forms import UserForm, CommentForm, ArticleForm


def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            request.session["user_id"] = user.id
            return redirect("/")
    else:
        form = UserForm()
    return render(request, "register.html", {"form": form})


def article_list(request):
    articles = Article.objects.all().order_by("-date")
    return render(request, "list.html", {"articles": articles})


def create_article(request):
    user_id = request.session.get("user_id")
    if not user_id:
        return redirect("/register")
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = User.objects.get(id=user_id)
            article.save()
            return redirect("/")
    else:
        form = ArticleForm()
    return render(request, "create.html", {"form": form})


def add_comment(request, article_id):
    user_id = request.session.get("user_id")
    if not user_id:
        return redirect("/register")

    article = get_object_or_404(Article, id=article_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author = User.objects.get(id=user_id)
            comment.save()
            return redirect("/")
    return redirect("/")
