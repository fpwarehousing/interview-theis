# Generated by Django 4.1.4 on 2022-12-09 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Forklift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_no', models.CharField(max_length=30, unique=True)),
                ('brand', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=30)),
                ('max_load', models.IntegerField(default=800)),
                ('hours_run', models.FloatField(default=0)),
                ('can_operate', models.BooleanField(default=True)),
                ('allowed_operators', models.JSONField(default=list)),
            ],
            options={
                'verbose_name': 'Forklift',
                'verbose_name_plural': 'Forklifts',
                'db_table': '',
                'managed': True,
            },
        ),
    ]