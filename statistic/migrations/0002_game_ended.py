# Generated by Django 4.0 on 2022-01-12 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='ended',
            field=models.BooleanField(default=False),
        ),
    ]
