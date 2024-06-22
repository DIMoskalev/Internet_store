from django.urls import path
from blog.apps import BlogConfig
from blog.views import (BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView,
                        BlogDeleteView)

app_name = BlogConfig.name

urlpatterns = [
    path('blog/create/', BlogCreateView.as_view(), name='blog_create'),
    path('', BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/update/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
    path('blog/<int:pk>/view/', BlogDetailView.as_view(), name='blog_view'),
]