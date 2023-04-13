from django.shortcuts import render
from main.models import Post
from .utils import *
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

class Post_list(DataMixin, ListView):
    model = Post
    template_name = 'main/post_list.html'
    context_object_name = 'posts'
    paginate_by = 1
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))

class Post_Detail(DataMixin, DetailView):
    model = Post
    template_name = 'main/post_detail.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'post'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Python bytes blog')
        return dict(list(context.items()) + list(c_def.items()))

class Category(DataMixin, ListView):
    model = Post
    template_name = 'main/post_list.html'
    context_object_name = 'posts'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Python bytes blog')
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])