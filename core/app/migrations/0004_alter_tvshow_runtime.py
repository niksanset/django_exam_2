# Generated by Django 5.0.6 on 2024-05-30 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_tvshow_ended_alter_tvshow_premiered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tvshow',
            name='runtime',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
