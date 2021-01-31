# Generated by Django 3.0.8 on 2021-01-27 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_auto_20210127_1024'),
        ('account', '0002_auto_20210126_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountuser',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.Department'),
        ),
        migrations.AlterField(
            model_name='accountuser',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.Organization'),
        ),
        migrations.AlterField(
            model_name='accountuser',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.Role'),
        ),
    ]
