# Generated by Django 3.0.8 on 2021-01-27 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_organization_registered_byuser_as'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='registered_byuser_as',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.Role', verbose_name='Admin'),
        ),
    ]
