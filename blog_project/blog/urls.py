from django.urls import path
from . import views

urlpatterns = [
    path('',views.article_list),
    path('register',views.register),
    path('create',views.create_article),
    path('article/<int:article_id>/comment', views.add_comment),
]
