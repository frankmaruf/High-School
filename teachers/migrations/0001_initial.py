# Generated by Django 3.1.4 on 2021-07-04 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school_information', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='Teachers')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('NID', models.BigIntegerField(unique=True)),
                ('birth_certificate', models.BigIntegerField(unique=True)),
                ('birthDate', models.DateField(null=True)),
                ('contract_number', models.CharField(max_length=11)),
                ('email', models.EmailField(blank=True, max_length=100)),
                ('father_name', models.CharField(max_length=150)),
                ('mother_name', models.CharField(max_length=150)),
                ('present_Address', models.CharField(max_length=250)),
                ('permanent_Address', models.CharField(max_length=250)),
                ('teaching_subjects', models.CharField(blank=True, max_length=200)),
                ('Join_Date', models.DateTimeField(auto_now=True)),
                ('Update_Date', models.DateTimeField(auto_now_add=True)),
                ('teaching_class', models.ManyToManyField(to='school_information.Class')),
                ('teaching_deaprtment', models.ManyToManyField(blank=True, to='school_information.Department')),
            ],
            options={
                'verbose_name_plural': 'Teachers List',
            },
        ),
    ]
