# Generated by Django 3.0.5 on 2020-08-16 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dav_app', '0003_auto_20200816_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onlineclass',
            name='c_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
