# Generated by Django 3.1.7 on 2021-04-23 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20210423_0806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='url',
            field=models.URLField(null=True, verbose_name='Url del sitio web'),
        ),
    ]
