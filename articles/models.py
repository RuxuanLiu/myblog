from django.db import models

# Create your models here.


class Tag(models.Model):
    content = models.CharField(max_length=100)

    def __str__(self):
        return self.content


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    pub_date = models.DateTimeField('date published')
    tag = models.ManyToManyField(Tag, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']


class Comment(models.Model):
    author = models.CharField(max_length=100)
    context = models.TextField(max_length=1000)
    pub_time = models.DateTimeField('pub time', auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.context[:20]

