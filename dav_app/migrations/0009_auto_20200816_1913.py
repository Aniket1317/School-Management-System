# Generated by Django 3.0.5 on 2020-08-16 13:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dav_app', '0008_auto_20200816_1902'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='onlineclass',
            name='ce_date',
        ),
        migrations.RemoveField(
            model_name='onlineclass',
            name='cs_date',
        ),
        migrations.RemoveField(
            model_name='onlinetest',
            name='te_date',
        ),
        migrations.RemoveField(
            model_name='onlinetest',
            name='ts_date',
        ),
        migrations.AddField(
            model_name='onlineclass',
            name='c_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='onlineclass',
            name='ce_time',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='onlineclass',
            name='cs_time',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='onlinetest',
            name='t_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='onlinetest',
            name='te_time',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='onlinetest',
            name='ts_time',
            field=models.TimeField(null=True),
        ),
    ]
