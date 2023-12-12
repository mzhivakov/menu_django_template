from django.db import models
from django.shortcuts import get_object_or_404

# Create your models here.

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_ancestor_urls(self):
        urls = [self.url]
        parent = self.parent
        while parent:
            urls.append(parent.url)
            parent = parent.parent
        return urls