# Generated by Django 5.0.2 on 2024-02-15 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0009_alter_studentmarks_st_mk"),
    ]

    operations = [
        migrations.AddField(
            model_name="studentmarks",
            name="Total",
            field=models.IntegerField(default=0),
        ),
    ]