from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Post(models.Model):
    """
    Stores a single blog post entry related to :model:`auth.User`.
    """
    category = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="blog_posts")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
        
    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        """
        Changes the post identifier format from ‘Post object (n)’ to a string literal 
        """
        return f"{self.title} | written by {self.author}"

class Comment(models.Model):
    """
    Stores a single comment entry related to :model:`auth.User` and :model:`blog.Post` 
    """
    post = models.ForeignKey(
    Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"