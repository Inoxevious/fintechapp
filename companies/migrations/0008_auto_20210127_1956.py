# Generated by Django 3.0.8 on 2021-01-27 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0007_auto_20210127_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanapplication',
            name='SK_ID_CURR',
            field=models.IntegerField(blank=True, max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='TARGET',
            field=models.IntegerField(blank=True, max_length=70, null=True),
        ),
    ]
