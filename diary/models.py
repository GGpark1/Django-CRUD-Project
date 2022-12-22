from django.db import models
from .validators import *


class Page(models.Model):
    title = models.CharField(max_length=100, validators=[validate_no_hash])
    content = models.TextField(validators=[validate_no_hash])
    feeling = models.CharField(max_length=80, validators=[validate_no_numbers])
    score = models.IntegerField(validators=[validation_score])
    dt_created = models.DateField(
        verbose_name="Date Created", auto_now_add=False)

    def __str__(self):
        return self.title
