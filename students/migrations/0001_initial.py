# Generated by Django 3.1.4 on 2021-02-13 04:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school_information', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='Student')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20)),
                ('roll', models.CharField(max_length=20)),
                ('birth_certificate', models.CharField(max_length=17)),
                ('birthDate', models.DateField(null=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('father_name', models.CharField(max_length=150)),
                ('mother_name', models.CharField(max_length=150)),
                ('father_NID', models.CharField(max_length=14)),
                ('mother_NID', models.CharField(max_length=14)),
                ('contract', models.CharField(max_length=11)),
                ('present_Address', models.CharField(max_length=250)),
                ('permanent_Address', models.CharField(max_length=250)),
                ('Join_Date', models.DateTimeField(auto_now=True)),
                ('Update_Date', models.DateTimeField(auto_now_add=True)),
                ('Class', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='school_information.class')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='school_information.department')),
                ('examiner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='school_information.examiner')),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='school_information.subject')),
                ('year', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='school_information.yearofstudent')),
            ],
            options={
                'verbose_name_plural': 'Student List',
            },
        ),
    ]
