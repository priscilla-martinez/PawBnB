# Generated by Django 4.0.3 on 2022-04-04 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_home_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='home_url',
            field=models.CharField(max_length=300),
        ),
    ]
