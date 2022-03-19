# Generated by Django 3.2.6 on 2021-08-23 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0002_auto_20210823_0503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='info',
            field=models.TextField(default='...', verbose_name='电影简介'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='logo',
            field=models.ImageField(upload_to='media/image/banner/%Y/%m', verbose_name='封面'),
        ),
    ]
