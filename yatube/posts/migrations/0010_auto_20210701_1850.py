# Generated by Django 2.2.19 on 2021-07-01 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, help_text='Загрузите изображение или просто перетащите файл', null=True, upload_to='posts/', verbose_name='Изображение'),
        ),
    ]