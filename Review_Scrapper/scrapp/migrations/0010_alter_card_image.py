# Generated by Django 4.2.1 on 2023-06-01 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapp', '0009_card_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='image',
            field=models.ImageField(default='', upload_to='static/images'),
        ),
    ]
