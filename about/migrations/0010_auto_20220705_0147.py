# Generated by Django 3.2.6 on 2022-07-05 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0009_alter_cancelrequest_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagescontactus',
            name='employee',
            field=models.CharField(default='-', max_length=255, null=True, verbose_name='Respuesta:'),
        ),
        migrations.AddField(
            model_name='messagescontactus',
            name='response',
            field=models.CharField(max_length=255, null=True, verbose_name='Respuesta:'),
        ),
        migrations.AddField(
            model_name='messagescontactus',
            name='status',
            field=models.CharField(default='Sin revisar', max_length=25, verbose_name='Estado:'),
        ),
    ]