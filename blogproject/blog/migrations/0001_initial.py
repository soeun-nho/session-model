# Generated by Django 4.2.1 on 2023-05-16 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=128, verbose_name="제목")),
                ("content", models.TextField(default="", verbose_name="내용")),
                ("date", models.DateTimeField(auto_now_add=True, verbose_name="작성일")),
            ],
        ),
    ]
