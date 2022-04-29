from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import About, Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView


def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3)  # По 3 статьи на каждой странице.
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, возвращаем первую страницу.
        posts = paginator.page(1)
    except EmptyPage:
        # Если номер страницы больше, чем общее количество страниц, возвращаем последнюю.
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'page': page, 'posts': posts})


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year,
                             publish__month=month, publish__day=day)

    return render(request, 'blog/post/detail.html', {'post': post})


def about_post_list(request):
    about_posts = About.published.all()
    return render(request, 'blog/about-post/about_list.html', {'about_posts': about_posts})



def about(request):
    return render(request, 'blog/about-post/about_list.html')


def post(request):
    return render(request, 'blog/post.html')

def contact(request):
    return render(request, 'blog/contact.html')


