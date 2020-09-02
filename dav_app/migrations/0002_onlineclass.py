# Generated by Django 3.0.5 on 2020-08-16 07:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dav_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OnlineClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std', models.CharField(max_length=5)),
                ('teacher_name', models.CharField(max_length=20)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('sub', models.CharField(max_length=10)),
            ],
        ),
    ]