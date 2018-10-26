from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Blog, Post, Comment

class IndexView(generic.ListView):
  template_name = 'blog/index.html'
  context_object_name = 'blog_list'

  def get_queryset(self):
    return Blog.objects.order_by('-created_at')

class DetailView(generic.DetailView):
  model = Blog
  template_name = 'blog/detail.html'

class PostDetailView(generic.DetailView):
  model = Post
  template_name = 'post/detail.html'
