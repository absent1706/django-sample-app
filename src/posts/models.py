from django.db import models
from django.contrib.auth.models import User


class PostCategory(models.TextChoices):
    IT = 'IT', 'IT'
    MISC = 'MISC', 'Misc'


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    category = models.CharField(
        max_length=10,
        choices=PostCategory.choices,
        default=PostCategory.MISC,
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'#{self.id}: {self.title} by {self.author}'