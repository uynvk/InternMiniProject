# Generated by Django 5.1.2 on 2024-11-06 03:47

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("icenter", "0007_alter_versiondetail_version"),
    ]

    operations = [
        migrations.RenameField(
            model_name="versiondetail",
            old_name="component_type",
            new_name="component",
        ),
        migrations.RemoveField(
            model_name="versiondetail",
            name="component_data_type",
        ),
    ]