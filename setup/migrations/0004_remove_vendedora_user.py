# Generated by Django 5.1.4 on 2024-12-28 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0003_alter_vendedora_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendedora',
            name='user',
        ),
    ]