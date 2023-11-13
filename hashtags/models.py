from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='Add hashtag')

    def __str__(self):
        return f'#{self.name}'

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True) #optional
    cost = models.PositiveIntegerField()
    tag = models.ManyToManyField(Tag, related_name='content_name')
    created_a = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}-{self.created_a}'

