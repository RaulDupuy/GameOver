# Generated by Django 3.2.6 on 2022-06-19 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_remove_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(null=True, upload_to='Produc Images'),
        ),
    ]
