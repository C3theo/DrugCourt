# Generated by Django 2.1.8 on 2020-01-25 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intake', '0002_auto_20200120_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='middle_initial',
            field=models.CharField(max_length=1),
        ),
    ]
