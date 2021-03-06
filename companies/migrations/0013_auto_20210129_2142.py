# Generated by Django 3.0.8 on 2021-01-29 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0012_auto_20210129_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan_history',
            name='AMT_ANNUITY',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='AMT_CREDIT',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='AMT_REQ_CREDIT_BUREAU_DAY',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='AMT_REQ_CREDIT_BUREAU_HOUR',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='AMT_REQ_CREDIT_BUREAU_MON',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='AMT_REQ_CREDIT_BUREAU_QRT',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='AMT_REQ_CREDIT_BUREAU_WEEK',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='AMT_REQ_CREDIT_BUREAU_YEAR',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='APARTMENTS_AVG',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='APARTMENTS_MEDI',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='APARTMENTS_MODE',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='BASEMENTAREA_AVG',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='BASEMENTAREA_MEDI',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='BASEMENTAREA_MODE',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='COMMONAREA_AVG',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='COMMONAREA_MEDI',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='COMMONAREA_MODE',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='DEF_30_CNT_SOCIAL_CIRCLE',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='DEF_60_CNT_SOCIAL_CIRCLE',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='ELEVATORS_AVG',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='ELEVATORS_MEDI',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='ELEVATORS_MODE',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='ENTRANCES_AVG',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='ENTRANCES_MEDI',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='ENTRANCES_MODE',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='EXT_SOURCE_1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='EXT_SOURCE_2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='EXT_SOURCE_3',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='FLOORSMAX_AVG',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='FLOORSMAX_MEDI',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='FLOORSMAX_MODE',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='FLOORSMIN_AVG',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='FLOORSMIN_MEDI',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='FLOORSMIN_MODE',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='LANDAREA_AVG',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='LANDAREA_MEDI',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='LANDAREA_MODE',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='LIVINGAPARTMENTS_AVG',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='LIVINGAPARTMENTS_MEDI',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='LIVINGAPARTMENTS_MODE',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='LIVINGAREA_AVG',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='LIVINGAREA_MEDI',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='LIVINGAREA_MODE',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='NONLIVINGAPARTMENTS_AVG',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='NONLIVINGAPARTMENTS_MEDI',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='NONLIVINGAPARTMENTS_MODE',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='NONLIVINGAREA_AVG',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='NONLIVINGAREA_MEDI',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='NONLIVINGAREA_MODE',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='OBS_30_CNT_SOCIAL_CIRCLE',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='OBS_60_CNT_SOCIAL_CIRCLE',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='OWN_CAR_AGE',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='REGION_POPULATION_RELATIVE',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='TOTALAREA_MODE',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='YEARS_BEGINEXPLUATATION_AVG',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='YEARS_BEGINEXPLUATATION_MEDI',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='YEARS_BEGINEXPLUATATION_MODE',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='YEARS_BUILD_AVG',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='YEARS_BUILD_MEDI',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan_history',
            name='YEARS_BUILD_MODE',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='AMT_ANNUITY',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='AMT_CREDIT',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='AMT_GOODS_PRICE',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='AMT_INCOME_TOTAL',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='APARTMENTS_AVG',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='APARTMENTS_MEDI',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='APARTMENTS_MODE',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='BASEMENTAREA_AVG',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='BASEMENTAREA_MEDI',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='BASEMENTAREA_MODE',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='COMMONAREA_AVG',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='COMMONAREA_MEDI',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='COMMONAREA_MODE',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='ELEVATORS_AVG',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='ELEVATORS_MEDI',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='ELEVATORS_MODE',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='ENTRANCES_AVG',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='ENTRANCES_MEDI',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='ENTRANCES_MODE',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='EXT_SOURCE_1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='EXT_SOURCE_2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='EXT_SOURCE_3',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='FLOORSMAX_AVG',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='FLOORSMAX_MEDI',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='FLOORSMAX_MODE',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='FLOORSMIN_AVG',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='FLOORSMIN_MEDI',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='FLOORSMIN_MODE',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='LANDAREA_AVG',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='LANDAREA_MEDI',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='LANDAREA_MODE',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='LIVINGAPARTMENTS_AVG',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='LIVINGAPARTMENTS_MEDI',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='LIVINGAPARTMENTS_MODE',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='LIVINGAREA_AVG',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='LIVINGAREA_MEDI',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='LIVINGAREA_MODE',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='NONLIVINGAPARTMENTS_AVG',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='NONLIVINGAPARTMENTS_MEDI',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='NONLIVINGAPARTMENTS_MODE',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='NONLIVINGAREA_AVG',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='NONLIVINGAREA_MEDI',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='NONLIVINGAREA_MODE',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='REGION_POPULATION_RELATIVE',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='TOTALAREA_MODE',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='YEARS_BEGINEXPLUATATION_AVG',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='YEARS_BEGINEXPLUATATION_MEDI',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='YEARS_BEGINEXPLUATATION_MODE',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='YEARS_BUILD_AVG',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='YEARS_BUILD_MEDI',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='YEARS_BUILD_MODE',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
