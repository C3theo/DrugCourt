# Generated by Django 3.0.1 on 2020-02-09 00:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('intake', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='client_num',
            new_name='client_id',
        ),
        migrations.AlterField(
            model_name='client',
            name='middle_initial',
            field=models.CharField(blank=True, max_length=1),
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('provider_type', models.CharField(choices=[('Drug Court', 'Drug Court'), ('Other', 'Other')], max_length=20)),
                ('clients', models.ManyToManyField(through='intake.Referral', to='intake.Client')),
            ],
        ),
        migrations.AddField(
            model_name='referral',
            name='provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='intake.Provider'),
        ),
    ]
