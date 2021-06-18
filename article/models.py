from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    body =models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()
#add thubmnail and authors
    def __str__(self):
        return self.title
    

    def snippet(self):
        return self.body[:50] + "..."
