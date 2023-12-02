# Generated by Django 4.2.4 on 2023-11-06 11:24

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="useraccount",
            name="groups",
        ),
        migrations.RemoveField(
            model_name="useraccount",
            name="user_permissions",
        ),
        migrations.AlterField(
            model_name="useraccount",
            name="avatar",
            field=models.ImageField(
                blank=True, null=True, upload_to=accounts.models.avatar_upload_path
            ),
        ),
        migrations.AlterField(
            model_name="useraccount",
            name="banner",
            field=models.ImageField(
                blank=True, null=True, upload_to=accounts.models.banner_upload_path
            ),
        ),
    ]
