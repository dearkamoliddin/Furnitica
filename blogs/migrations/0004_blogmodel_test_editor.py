# Generated by Django 5.0.7 on 2024-07-20 09:27

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_blogmodel_short_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='test_editor',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]