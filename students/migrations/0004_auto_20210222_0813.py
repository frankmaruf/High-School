# Generated by Django 3.1.4 on 2021-02-22 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20210222_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='birth_certificate',
            field=models.CharField(max_length=17, unique=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='contract',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='students',
            name='father_NID',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='students',
            name='mother_NID',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='students',
            name='roll',
            field=models.CharField(max_length=20),
        ),
    ]