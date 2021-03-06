# Generated by Django 3.0.2 on 2020-04-17 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nurse', '0004_auto_20200417_1619'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nurse',
            name='area',
        ),
        migrations.RemoveField(
            model_name='nurse',
            name='fullName',
        ),
        migrations.AlterField(
            model_name='nurse',
            name='latitude',
            field=models.FloatField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='nurse',
            name='longitude',
            field=models.FloatField(default=0, max_length=10),
        ),
    ]
