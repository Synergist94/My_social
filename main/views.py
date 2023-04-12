from django.shortcuts import render
from main.models import Post
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

class post_list(ListView):
    model = Post
    template_name = 'main/index.html'
