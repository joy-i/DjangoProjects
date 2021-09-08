from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField()
    body = models.TextField(max_length=500)
    date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:100] + "..."