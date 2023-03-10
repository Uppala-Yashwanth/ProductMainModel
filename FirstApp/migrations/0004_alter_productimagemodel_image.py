# Generated by Django 4.1.1 on 2023-01-18 12:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0003_alter_productmainmodel_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimagemodel',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'mp4', 'mp3', 'pdf', 'txt'])]),
        ),
    ]
