# Generated by Django 4.1.7 on 2023-02-20 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='location',
            new_name='locations',
        ),
    ]