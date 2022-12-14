# Generated by Django 4.0.6 on 2022-07-26 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('author', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('tag', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rep', models.TextField()),
                ('author_rep', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Qapps.question')),
            ],
        ),
    ]
