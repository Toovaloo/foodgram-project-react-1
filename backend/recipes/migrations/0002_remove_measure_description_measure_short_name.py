# Generated by Django 4.0 on 2021-12-08 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='measure',
            name='description',
        ),
        migrations.AddField(
            model_name='measure',
            name='short_name',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Сокращение'),
        ),
    ]
