# Generated by Django 4.1.5 on 2023-01-18 17:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TPO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='TPR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('type', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('time', models.DateTimeField(default=datetime.datetime(2023, 1, 18, 17, 31, 11, 830214, tzinfo=datetime.timezone.utc))),
                ('tpo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tpo.tpo')),
                ('tpr', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tpo.tpr')),
            ],
        ),
    ]
