# Generated by Django 5.1 on 2024-08-20 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0026_post_model_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post_model',
            name='post_image',
            field=models.ImageField(default='post_image/jorge-zapata-4nXkhLCrkLo-unsplash.jpg', upload_to='post_image/'),
        ),
    ]
