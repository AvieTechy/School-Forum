# Generated by Django 4.0.6 on 2022-07-26 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Qapps', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Question',
            new_name='Questions',
        ),
        migrations.RenameModel(
            old_name='Reply',
            new_name='Replys',
        ),
    ]