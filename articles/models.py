from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    time = models.DateTimeField()
    content = models.TextField(max_length=5000)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title



