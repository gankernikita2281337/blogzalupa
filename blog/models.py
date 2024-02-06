from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=128,verbose_name='Title')
    text = models.TextField(verbose_name='Text')
    created_date = models.DateTimeField(auto_now_add=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'
