# Generated by Django 4.1.3 on 2022-12-03 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_alter_catalog_options_alter_catalog_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='image',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='price',
            field=models.FloatField(verbose_name='Цена'),
        ),
    ]
