from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=125)  # max_length is required field for CharField
    author = models.CharField(max_length=100)
    description = models.TextField()
    image = models.URLField(null=True,blank=True) # null means can be empty in db, blank means field can be empty without validation errors
    created = models.DateTimeField(auto_now_add=True)  # putting time stamp right now; any time recipe added, will set this field to current date
    updated = models.DateTimeField(auto_now=True)
    # auto now updates every time save
    # auto now add updates upon record creation

    def __str__(self):
        return f"{self.name}"


class Measure(models.Model):
    name = models.CharField(max_length=30, unique=True)
    abbreviation = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.name}"


class FoodItem(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Ingredient(models.Model):
    amount = models.FloatField
    recipe = models.ForeignKey("Recipe",
        related_name="ingredients",
        on_delete=models.CASCADE)
    measure = models.ForeignKey("Measure",
        related_name="measure",
        on_delete=models.PROTECT)
    food = models.ForeignKey("FoodItem",
        related_name="food",
        on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.food}"

class Step(models.Model):
    recipe = models.ForeignKey("Recipe",
    related_name="steps", on_delete=models.CASCADE)
    order = models.SmallIntegerField()
    directions = models.CharField(max_length=300)
    food_items = models.ManyToManyField("FoodItem", null=True, blank=True)
    #  used to create a relationship to another model (i.e. one recipe will have many steps); relates this back to recipe model (one-to-many)
    #  either ("Recipe") OR (Recipe) works ... convention is name of model as a strin
    #  CASCASE causes all steps for recipe to be deleted if receipe is deleted
    #  related_name="steps"; attribute specifies the name of the reverse relation from the User model back to your model

    def __str__(self):
        return f"{self.order}"
