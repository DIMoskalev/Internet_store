from django.urls import path
from blog.apps import BlogConfig
from blog.views import (BlogArticleCreateView, BlogArticleListView, BlogArticleDetailView, BlogArticleUpdateView,
                        BlogArticleDeleteView)

app_name = BlogConfig.name

urlpatterns = [
    path('create/', BlogArticleCreateView.as_view(), name='blog_create'),
    path('', BlogArticleListView.as_view(), name='blog_list'),
    path('delete/<int:pk>/', BlogArticleDeleteView.as_view(), name='blog_delete'),
    path('edit/<int:pk>/', BlogArticleUpdateView.as_view(), name='blog_edit'),
    path('view/<int:pk>/', BlogArticleDetailView.as_view(), name='blog_view'),
]