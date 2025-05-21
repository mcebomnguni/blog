from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=140)  
    body = models.TextField()  
    date = models.DateTimeField(auto_now_add=True)  
    signature = models.CharField(max_length=140, default="Love One Another as I Have Loved You")  

    def __str__(self):
        return self.title
