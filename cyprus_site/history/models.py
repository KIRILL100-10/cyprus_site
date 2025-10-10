from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Category Name')
    slug = models.SlugField(max_length=100, unique=True, blank=True, verbose_name='Category Slug')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('name',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})


class Article(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='Title')
    slug = models.SlugField(max_length=100, unique=True, blank=True, verbose_name='Slug')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True, related_name='articles', verbose_name='Category')
    image = models.ImageField(upload_to='history/%Y/%m/%d', null=True, blank=True, verbose_name='Image')
    content = models.TextField(verbose_name='Content')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('article', kwargs={'article_slug': self.slug})


class Comment(models.Model):
    article = models.ForeignKey('Article', on_delete=models.SET_NULL, null=True, related_name='comments', verbose_name='Article')
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name='comments', verbose_name='Author')
    text = models.TextField(verbose_name='Comment')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.author}: {self.text[:25]}'
