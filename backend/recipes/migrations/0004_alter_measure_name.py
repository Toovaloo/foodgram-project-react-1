# Generated by Django 4.0 on 2021-12-08 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_remove_measure_short_name_measure_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measure',
            name='name',
            field=models.CharField(max_length=10, unique=True, verbose_name='Название'),
        ),
    ]
