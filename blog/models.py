from django.db import models

class Post(models.Model):
    """
    A blog post model representing individual entries in the blog.

    Attributes:
        title (CharField): The title of the blog post (max 140 characters).
        body (TextField): The main content of the blog post.
        date (DateTimeField): The date and time the post was created (auto-set on creation).
        signature (CharField): A short quote or signature line (default provided).
    """
    title = models.CharField(max_length=140)  
    body = models.TextField()  
    date = models.DateTimeField(auto_now_add=True)  
    signature = models.CharField(max_length=140, default="Love One Another as I Have Loved You")  

    def __str__(self):
        return self.title
