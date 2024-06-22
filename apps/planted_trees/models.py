from django.db import models

from apps.core.models import BaseModel
from apps.accounts.models import User
from apps.trees.models import Tree


class PlantedTree(BaseModel):
    age = models.IntegerField(
        blank=True, null=True
    )
    tree = models.ForeignKey(Tree, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return f'Plated user {self.user.account.email} | Tree {self.tree.name}'

    class Meta:
        verbose_name = 'PlantedTree'
        verbose_name_plural = 'PlantedTrees'
        ordering = ['-created_at']
        db_table = 'planted_tree'
