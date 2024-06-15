# Generated by Django 5.0.6 on 2024-06-06 13:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apliko', '0009_alter_vidbendo_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vidbendo',
            name='upload',
            field=models.FileField(blank=True, null=True, upload_to='source_video/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg'])]),
        ),
    ]
