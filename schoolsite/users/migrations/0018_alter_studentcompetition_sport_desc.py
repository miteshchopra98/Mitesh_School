# Generated by Django 5.0.2 on 2024-02-16 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0017_alter_studentcompetition_comp"),
    ]

    operations = [
        migrations.AlterField(
            model_name="studentcompetition",
            name="sport_desc",
            field=models.TextField(default="desc", max_length=1000),
        ),
    ]
