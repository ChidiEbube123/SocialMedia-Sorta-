# Generated by Django 5.1 on 2024-08-20 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0017_alter_post_model_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_model',
            name='post_image',
            field=models.ImageField(blank=True, upload_to='post_images/'),
        ),
    ]
