# Generated by Django 4.1.1 on 2023-03-13 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="resultu2018",
            name="credit_unit",
            field=models.DecimalField(decimal_places=2, default=3, max_digits=5),
        ),
    ]
