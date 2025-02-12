# Generated by Django 5.1.3 on 2024-11-21 16:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("diary", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="diary",
            name="emotion_analysis",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="diary",
                to="diary.emotionanalysis",
            ),
        ),
    ]
