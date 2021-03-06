# Generated by Django 3.0.2 on 2020-04-08 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nurse', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nurse',
            name='lattiude',
            field=models.FloatField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='nurse',
            name='longitude',
            field=models.FloatField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='nurse',
            name='postCode',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='nurse',
            name='email',
            field=models.EmailField(max_length=100, null=True),
        ),
    ]
