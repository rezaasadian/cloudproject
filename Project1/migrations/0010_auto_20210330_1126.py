# Generated by Django 3.1.7 on 2021-03-30 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Project1', '0009_auto_20210330_1120'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visitstatus',
            old_name='status',
            new_name='type',
        ),
    ]
