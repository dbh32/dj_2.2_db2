# Generated by Django 2.1.1 on 2019-11-05 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20191105_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='relationship',
            name='tag_main',
            field=models.BooleanField(default=False, verbose_name='Основной тег'),
        ),
    ]
