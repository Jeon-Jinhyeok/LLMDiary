# Generated by Django 5.1.3 on 2024-11-19 13:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0005_alter_person_login_id_alter_person_login_pw_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="person",
            name="last_login",
            field=models.DateTimeField(
                blank=True, default=django.utils.timezone.now, null=True
            ),
        ),
    ]
