# Generated by Django 3.1.2 on 2020-11-22 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='currency_code',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]
