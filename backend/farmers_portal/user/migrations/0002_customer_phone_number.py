# Generated by Django 3.0.3 on 2020-02-06 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='phone_number',
            field=models.IntegerField(default=877, unique=True),
            preserve_default=False,
        ),
    ]
