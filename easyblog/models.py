from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    timestamp = models.DateTimeField()

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','timestamp')

admin.site.register(BlogPost,BlogPostAdmin)
