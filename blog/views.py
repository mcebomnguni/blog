from django.views.generic import ListView, DetailView
from .models import Post

class PostListView(ListView):
    queryset = Post.objects.all().order_by('-date')[:25]
    template_name = "blog.html"

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
