from django.views.generic import DetailView, ListView ## um lista 1 detalhado e outro lista todas views

from .models import Post

class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post