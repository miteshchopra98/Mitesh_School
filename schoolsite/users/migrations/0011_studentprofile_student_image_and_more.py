# Generated by Django 5.0.2 on 2024-02-16 08:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0010_studentmarks_total"),
    ]

    operations = [
        migrations.AddField(
            model_name="studentprofile",
            name="student_image",
            field=models.ImageField(
                default="std_default.jpg",
                height_field=200,
                upload_to="student_pictures",
                width_field=150,
            ),
        ),
        migrations.AddField(
            model_name="teacherprofile",
            name="teacher_image",
            field=models.ImageField(
                default="teach_default.jpg",
                height_field=200,
                upload_to="teacher_pictures",
                width_field=150,
            ),
        ),
        migrations.CreateModel(
            name="StudentCompetition",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sport", models.CharField(default=None, max_length=20)),
                (
                    "sport_image",
                    models.ImageField(
                        default="default.jpg",
                        height_field=200,
                        upload_to="competition_pictures",
                        width_field=150,
                    ),
                ),
                (
                    "comp",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.student"
                    ),
                ),
            ],
        ),
    ]