# Generated by Django 3.2.6 on 2022-07-03 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_alter_userprofile_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Número de teléfono:'),
        ),
    ]