# Generated by Django 3.1.4 on 2021-02-22 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_information', '0002_auto_20210213_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yearofstudent',
            name='year',
            field=models.PositiveSmallIntegerField(),
        ),
    ]