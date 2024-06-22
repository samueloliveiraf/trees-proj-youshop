from django.db import models

from apps.core.models import BaseModel


class Tree(BaseModel):
    name = models.CharField(
        max_length=2048
    )
    scientific_name = models.CharField(
        max_length=2048,
        blank=True, null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tree'
        verbose_name_plural = 'Trees'
        ordering = ['-created_at']
        db_table = 'trees'
