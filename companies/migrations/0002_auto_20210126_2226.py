# Generated by Django 3.0.8 on 2021-01-26 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='name',
        ),
        migrations.AddField(
            model_name='organization',
            name='business_name',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='business_trading_name',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='total_branches',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
