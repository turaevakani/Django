from django.db import models


class Book(models.Model):
    GENRE = (
        ('Роман', 'Роман'),
        ('Приключения', 'Приключения'),
        ('Триллер', 'Триллер'),
        ('Фантастика', 'Фантастика'),
        ('Детектив', 'Детектив'),
    )

    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    genre = models.CharField(max_length=100, choices=GENRE, default=GENRE[0], null=True)
    video = models.URLField(null=True)
    cost = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ReviewBook(models.Model):
    STARS = (
        ('*', '*'),
        ('**', '**'),
        ('***', '***'),
        ('****', '****'),
        ('*****', '*****'),

    )
    title_book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='review_object')
    text_review = models.TextField()
    rate_stars = models.CharField(max_length=100, choices=STARS)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.title_book}"
