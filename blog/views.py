from django.shortcuts import render
from .models import Article
from .forms import PostForm

def index(request):
    recent_list = Article.objects.order_by('created_date').reverse()[:4]
    return render(request, 'blog/index.html', {'recent_list': recent_list})

def poetry_list(request):
    poetry_list = Article.objects.all()
    return render(request, 'blog/list.html', {'poetry_list': poetry_list})

def post_new(request):
    if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save()
                return render(request, 'blog/index.html', {})
    else:
        form = PostForm()
    return render(request, 'blog/add.html', {'form': form})