# Generated by Django 5.1.2 on 2024-11-06 03:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("icenter", "0006_alter_apiactiveversion_api_alter_apiversion_api"),
    ]

    operations = [
        migrations.AlterField(
            model_name="versiondetail",
            name="version",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="details",
                to="icenter.apiversion",
            ),
        ),
    ]