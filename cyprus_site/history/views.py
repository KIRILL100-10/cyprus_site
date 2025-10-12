from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework.generics import get_object_or_404
from rest_framework.reverse import reverse_lazy

from history.forms import CommentForm
from history.models import Article, Category, Comment


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        return context


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


class CommentDetail(LoginRequiredMixin, DetailView):
    model = Comment
    pk_url_kwarg = 'comment_id'
    context_object_name = 'comment'
    template_name = 'history/comment_detail.html'


class CreateComment(LoginRequiredMixin, CreateView):
    form_class = CommentForm
    template_name = 'history/create_comment.html'

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.article = get_object_or_404(Article, slug=self.kwargs['article_slug'])
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('history:article_detail', kwargs={'article_slug': self.kwargs['article_slug']})


class EditComment(LoginRequiredMixin, UpdateView):
    form_class = CommentForm
    model = Comment
    pk_url_kwarg = 'comment_id'
    template_name = 'history/comment_update.html'

    def get_success_url(self):
        return reverse_lazy('history:article_detail', kwargs={'article_slug': self.kwargs['article_slug']})


class DeleteComment(LoginRequiredMixin, DeleteView):
    model = Comment
    pk_url_kwarg = 'comment_id'
    template_name = 'history/comment_delete.html'

    def get_success_url(self):
        return reverse_lazy('history:article_detail', kwargs={'article_slug': self.kwargs['article_slug']})
