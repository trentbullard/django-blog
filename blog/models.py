from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
  owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
  name = models.CharField(max_length=200)
  notes = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return "(%s) %s" % (self.id, self.name)

class Post(models.Model):
  author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
  blog = models.ForeignKey(Blog, on_delete=models.SET_NULL, blank=True, null=True)
  title = models.CharField(max_length=200)
  content = models.TextField()
  notes = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return "(%s) %s" % (self.id, self.title)

class Comment(models.Model):
  owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
  post = models.ForeignKey(Post, on_delete=models.SET_NULL, blank=True, null=True)
  parent_comment = models.ForeignKey("Comment", on_delete=models.SET_NULL, blank=True, null=True)
  content = models.TextField()
  notes = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return "(%s) %s" % (self.id, self.content)
