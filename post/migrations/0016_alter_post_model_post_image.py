# Generated by Django 5.1 on 2024-08-19 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0015_alter_post_model_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_model',
            name='post_image',
            field=models.ImageField(default='post_images/FB_IMG_16607757619264546.jpg', upload_to='post_images/'),
        ),
    ]
