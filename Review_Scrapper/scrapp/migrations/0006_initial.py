# Generated by Django 4.2.1 on 2023-06-01 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('scrapp', '0005_delete_card'),
    ]

    operations = [
        migrations.CreateModel(
            name='card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rating', models.IntegerField(max_length=10)),
                ('subject', models.CharField(max_length=80)),
                ('desc', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]