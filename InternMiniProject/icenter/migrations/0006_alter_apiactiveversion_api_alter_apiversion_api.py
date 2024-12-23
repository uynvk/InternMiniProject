# Generated by Django 5.1.2 on 2024-11-05 07:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("icenter", "0005_remove_apiactiveversion_unique_api_version_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="apiactiveversion",
            name="api",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="version",
                to="icenter.api",
            ),
        ),
        migrations.AlterField(
            model_name="apiversion",
            name="api",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="versions",
                to="icenter.api",
            ),
        ),
    ]
