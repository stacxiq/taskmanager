# Generated by Django 3.2 on 2021-06-04 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image_url',
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
