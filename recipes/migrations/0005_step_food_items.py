# Generated by Django 4.1 on 2022-08-24 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0004_ingredient"),
    ]

    operations = [
        migrations.AddField(
            model_name="step",
            name="food_items",
            field=models.ManyToManyField(blank=True, null=True, to="recipes.fooditem"),
        ),
    ]