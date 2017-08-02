from django.db import models
from django.utils import timezone

class Article(models.Model):
    author_name = models.CharField(max_length=35)
    title = models.CharField(max_length=100)
    poetry_text = models.TextField(default="poetry")
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def __str__():
        return self.title
