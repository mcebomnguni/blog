from django.views.generic import ListView, DetailView
from .models import Post

class PostListView(ListView):
    """
    Display a list of the most recent blog posts.

    Attributes:
        queryset (QuerySet): A queryset of the 25 most recent posts ordered by date.
        template_name (str): The template used to render the list of posts.
    """
    queryset = Post.objects.all().order_by('-date')[:25]
    template_name = "blog.html"

class PostDetailView(DetailView):
    """
    Display detailed view of a single blog post.

    Attributes:
        model (Model): The model class to use for retrieving the blog post.
        template_name (str): The template used to render the blog post details.
    """
    model = Post
    template_name = "blog/post_detail.html"
