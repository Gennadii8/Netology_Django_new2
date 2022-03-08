from django.db.models import Prefetch
from django.shortcuts import render

from articles.models import Article, ArticleScope


def articles_list(request):
    template = 'articles/news.html'
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'
    articles = Article.objects.order_by(ordering).prefetch_related(
        Prefetch('scopes',
                 queryset=
                 ArticleScope.objects.order_by('-is_main').select_related('tag_name')))

    context = {'object_list': articles}
    return render(request, template, context)
