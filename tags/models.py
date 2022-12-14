from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=20)
    recipes = models.ManyToManyField("recipes.Recipe",
        related_name="tags")  # go into recipes, grab Recipe

    def __str__(self):
        return f"{self.name}"
