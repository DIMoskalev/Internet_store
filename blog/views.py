from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from blog.models import BlogArticle


class BlogArticleCreateView(CreateView):
    model = BlogArticle
    fields = ('title', 'content', 'preview', )
    success_url = reverse_lazy('blog:blog_list')


class BlogArticleListView(ListView):
    model = BlogArticle


class BlogArticleDetailView(DetailView):
    model = BlogArticle


class BlogArticleUpdateView(UpdateView):
    model = BlogArticle
    fields = ('title', 'content', 'preview', )


class BlogArticleDeleteView(DeleteView):
    model = BlogArticle
    success_url = reverse_lazy('blog:blog_list')
