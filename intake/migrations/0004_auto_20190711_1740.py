# Generated by Django 2.1.8 on 2019-07-11 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intake', '0003_auto_20190711_1716'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='decision',
            options={'managed': True, 'permissions': [('can_decide', 'Can Decide')]},
        ),
    ]
