# Generated by Django 5.0.2 on 2024-02-16 09:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0016_alter_studentcompetition_comp"),
    ]

    operations = [
        migrations.AlterField(
            model_name="studentcompetition",
            name="comp",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.student",
            ),
        ),
    ]
