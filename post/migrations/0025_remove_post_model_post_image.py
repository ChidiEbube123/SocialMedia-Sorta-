# Generated by Django 5.1 on 2024-08-20 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0024_alter_post_model_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post_model',
            name='post_image',
        ),
    ]
