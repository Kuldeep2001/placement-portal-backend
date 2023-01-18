# Generated by Django 4.1.5 on 2023-01-17 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('Cluster_id', models.IntegerField(primary_key=True, serialize=False)),
                ('starting', models.FloatField(default=0)),
                ('ending', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('board', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('first_name', models.CharField(max_length=100)),
                ('roll', models.BigIntegerField(primary_key=True, serialize=False)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('college_email', models.EmailField(max_length=254)),
                ('personal_email', models.EmailField(max_length=254)),
                ('gender', models.CharField(default='', max_length=100)),
                ('pnumber', models.BigIntegerField()),
                ('pincode', models.BigIntegerField()),
                ('batch_year', models.IntegerField()),
                ('resume', models.CharField(default='', max_length=200)),
                ('undertaking', models.CharField(default='', max_length=200)),
                ('cgpi', models.FloatField(default=0)),
                ('class_10_year', models.IntegerField()),
                ('class_10_perc', models.FloatField()),
                ('class_12_year', models.IntegerField()),
                ('class_12_perc', models.FloatField()),
                ('active_backlog', models.SmallIntegerField()),
                ('total_backlog', models.SmallIntegerField()),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.specialization')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.category')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.city')),
                ('cluster_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cluster_1', to='student.cluster')),
                ('cluster_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cluster_2', to='student.cluster')),
                ('cluster_3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cluster_3', to='student.cluster')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.country')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.state'),
        ),
    ]
