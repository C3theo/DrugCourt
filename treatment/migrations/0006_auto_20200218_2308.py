# Generated by Django 2.1.8 on 2020-02-19 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treatment', '0005_auto_20200218_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectives',
            name='description',
            field=models.TextField(max_length=250),
        ),
    ]
