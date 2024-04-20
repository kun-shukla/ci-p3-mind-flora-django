from cloudinary.models import CloudinaryField
from django.db import models
from django.contrib.auth.models import User


STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    """
    Stores a single blog post entry related to :model:`auth.User`.
    """
    category = models.CharField(max_length=50)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="blog_posts")
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
        
    class Meta:
        ordering = ["category","created_on"]

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

class About(models.Model):
    """
    Stores a single About section entry
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

class AboutSectionNavImage(models.Model):
    """
    Stores a single About section (circular) nav image/title using a Cloudinary image field 
    """
    title = models.CharField(max_length=50)
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

class ShareDiscoveryFormBgVid(models.Model):
    """
    Stores a single Form section background video using a Cloudinary video field
    """
    title = models.CharField(max_length=50)
    featured_video = CloudinaryField('video', resource_type='video')

    def __str__(self):
        return f"{self.title} video uploaded"
   

class UserRecommendedDestination(models.Model):
    """
    Stores a single user-recommended destination message
    """
    full_Name = models.CharField(max_length=200)
    email = models.EmailField()
    category = models.TextField()
    destination = models.CharField(max_length=200)
    description = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Travel destination recommended by {self.full_Name}"