from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.views.generic import ListView, DetailView
from rest_framework.generics import get_object_or_404

from history.models import Article, Category


class ArticleList(LoginRequiredMixin, ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'history/article_list.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.annotate(total=Count('articles')).filter(total__gt=0)
        return context


class ArticleDetail(LoginRequiredMixin, DetailView):
    model = Article
    context_object_name = 'article'
    slug_url_kwarg = 'article_slug'
    template_name = 'history/article_detail.html'


class ArticleCategory(LoginRequiredMixin, ListView):
    model = Category
    context_object_name = 'articles'
    template_name = 'history/article_category.html'
    paginate_by = 3

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs['category_slug'])
        return category.articles.all()


class ArticleSearch(LoginRequiredMixin, ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'history/article_search.html'
    paginate_by = 3

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            articles = Article.objects.filter(title__icontains=query)
            return articles
        else:
            return Article.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context
