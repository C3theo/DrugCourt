# Generated by Django 2.1.8 on 2020-02-19 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treatment', '0004_auto_20200218_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectives',
            name='description',
            field=models.TextField(max_length=150),
        ),
    ]
