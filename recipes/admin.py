from django.contrib import admin
from recipes.models import Recipe, Step, Measure, FoodItem, Ingredient

# Register your models here.

admin.site.register(Recipe)
admin.site.register(Step)
admin.site.register(Measure) # must register here to see it on /admin
admin.site.register(FoodItem)
admin.site.register(Ingredient)
