# Generated by Django 2.1.8 on 2019-05-31 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('viewflow', '0006_i18n'),
    ]

    operations = [
        migrations.CreateModel(
            name='HelloWorldProcess',
            fields=[
                ('process_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='viewflow.Process')),
                ('text', models.CharField(max_length=150)),
                ('approved', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('viewflow.process',),
        ),
    ]
