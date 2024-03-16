from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Author(models.Model):
    fullname = models.CharField(max_length=200, unique=True)
    born_date = models.DateField()
    born_location = models.CharField(max_length=300)
    author_description = models.CharField(max_length=10000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    author_created = models.DateTimeField(auto_now_add=True)


class Tag(models.Model):
    name = models.CharField(max_length=25, null=False, unique=True)
    # region - add user relation
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'name'],
                name='tag of username'
            )
        ]

    # endregion

    def __str__(self):
        return f"{self.name}"


class Quote(models.Model):
    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=150, null=False)
    done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    # region - add user relation
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=1)

    # endregion

    def __str__(self):
        return f"{self.name}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['author', 'name'],
                                    name='author quote')
        ]
