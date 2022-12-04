# Generated by Django 4.1.3 on 2022-12-03 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_catalog'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='catalog',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Информация о товарах'},
        ),
        migrations.AlterField(
            model_name='catalog',
            name='image',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='product_name',
            field=models.CharField(max_length=50, verbose_name='Краткое название'),
        ),
    ]
