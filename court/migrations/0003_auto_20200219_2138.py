# Generated by Django 2.1.8 on 2020-02-20 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('court', '0002_auto_20200219_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feehistory',
            name='comments',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='feehistory',
            name='submit_by',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='phasehistory',
            name='phase',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='sanctions',
            name='comm_srvc_name',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='sanctions',
            name='sanc_desc',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='screens',
            name='result',
            field=models.CharField(max_length=250),
        ),
    ]
