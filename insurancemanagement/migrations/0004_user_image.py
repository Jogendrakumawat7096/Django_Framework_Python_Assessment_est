# Generated by Django 5.0 on 2023-12-23 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurancemanagement', '0003_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default='img', upload_to='profile_image/'),
        ),
    ]
