# Generated by Django 4.2.2 on 2023-08-16 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0002_branches'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('job_id', models.AutoField(primary_key=True, serialize=False)),
                ('job_name', models.CharField(blank=True, max_length=30)),
                ('max_salary', models.IntegerField(blank=True)),
                ('mini_salary', models.IntegerField(blank=True)),
            ],
            options={
                'db_table': 'JOBS',
                'ordering': ['job_id'],
            },
        ),
    ]
