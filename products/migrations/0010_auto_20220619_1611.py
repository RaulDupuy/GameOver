# Generated by Django 3.2.6 on 2022-06-19 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_products_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='Produc Images'),
        ),
        migrations.AddField(
            model_name='products',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='Produc Images'),
        ),
        migrations.AddField(
            model_name='products',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='Produc Images'),
        ),
        migrations.AddField(
            model_name='products',
            name='image5',
            field=models.ImageField(blank=True, null=True, upload_to='Produc Images'),
        ),
    ]