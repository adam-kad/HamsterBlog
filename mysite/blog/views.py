from tokenize import Number
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import About, Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm
from mysite.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL
from taggit.models import Tag
from django.db.models import Count



def contact_view(request):
    # если метод GET, вернем форму
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        # если метод POST, проверим форму и отправим письмо
        form = ContactForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            your_name = form.cleaned_data['your_name']
            try:
                send_mail(f'Номер: {number} Эл.адрес {from_email} Имя: {your_name}', message,
                          DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            return redirect('/success')
    else:
        return HttpResponse('Неверный запрос.')
    return render(request, "blog/contact.html", {'form': form})



def success_view(request):
    return render(request, "blog/contact.html")



def post_list(request, tag_slug=None):
    object_list = Post.published.all()
    tag = None
    
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

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
    return render(request, 'blog/post/list.html', {'page': page, 'posts': posts, 'tag': tag})


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year,
                             publish__month=month, publish__day=day)

    # Формирование списка похожих статей.
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids)\
                                    .exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags'))\
                                    .order_by('-same_tags','-publish')[:4]


    return render(request, 'blog/post/detail.html', {'post': post, 'similar_posts': similar_posts})


def about_post_list(request):
    about_posts = About.published.all()
    return render(request, 'blog/about-post/about_list.html', {'about_posts': about_posts})



def about(request):
    return render(request, 'blog/about-post/about_list.html')


def post(request):
    return render(request, 'blog/post.html')

#def contact(request):
#    return render(request, 'blog/contact.html')


