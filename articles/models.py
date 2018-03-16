from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']


class Tag(models.Model):
    content = models.CharField(max_length=100)

    def __str__(self):
        return self.content



