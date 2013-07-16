from django.db import models
from django.contrib import admin

class Post(models.Model):
    title=models.CharField(max_length=255)
    datetime=models.DateTimeField(u'Publication date')
    content=models.TextField(max_length=10000)
    class Meta:
        ordering=('-datetime',)
class BlogPostAdmin(admin.ModelAdmin):
    list_display=('title', 'datetime')
    
admin.site.register(Post, BlogPostAdmin)

