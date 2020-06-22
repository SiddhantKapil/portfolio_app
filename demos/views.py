from django.shortcuts import render
from .models import Post
from django.views.generic import  ListView
# Create your views here.
def home(request):
    context = {
        "posts": Post.objects.all()
               }
    return render(request, 'demos/home.html', context)
class PostListView(ListView):
    model = Post
    template_name = 'demos/home.html'
    context_object_name = "posts"
    # ordering = ['-date_posted']

def about(request):
    return render(request, 'demos/about.html', {'title': 'About'})