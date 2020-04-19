from django.conf import settings
from django.db import models
from django.utils import timezone


class Article(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
    company = models.CharField(max_length=200)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title