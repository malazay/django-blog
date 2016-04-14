from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from re import split


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return "/categories/%s" % self.slug


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)
    text = models.TextField()
    tags = models.CharField(max_length=300)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    categories = models.ManyToManyField(Category, blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_tag_list(self):
        return split(';|; |,|, |\*|\n', self.tags)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        if self.published_date:
            return "%s/%s/%s/" % (self.published_date.year, self.published_date.month, self.slug)
        else:
            return "%s/%s/%s/" % (self.created_date.year, self.created_date.month, self.slug)


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text



