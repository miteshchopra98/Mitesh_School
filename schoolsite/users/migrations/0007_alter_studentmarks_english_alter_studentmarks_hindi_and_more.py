# Generated by Django 5.0.2 on 2024-02-15 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_studentmarks"),
    ]

    operations = [
        migrations.AlterField(
            model_name="studentmarks",
            name="English",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="studentmarks",
            name="Hindi",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="studentmarks",
            name="Marathi",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="studentmarks",
            name="Maths",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="studentmarks",
            name="Science",
            field=models.IntegerField(default=0),
        ),
    ]
