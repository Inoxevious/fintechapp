# Generated by Django 3.0.8 on 2021-01-29 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0009_auto_20210127_1959'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan_History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LOAN_ID', models.IntegerField(blank=True, null=True)),
                ('NAME_CONTRACT_TYPE', models.CharField(blank=True, max_length=70, null=True)),
                ('CODE_GENDER', models.CharField(blank=True, max_length=70, null=True)),
                ('FLAG_OWN_CAR', models.CharField(blank=True, max_length=70, null=True)),
                ('FLAG_OWN_REALTY', models.CharField(blank=True, max_length=70, null=True)),
                ('NAME_TYPE_SUITE', models.CharField(blank=True, max_length=70, null=True)),
                ('NAME_INCOME_TYPE', models.CharField(blank=True, max_length=70, null=True)),
                ('NAME_EDUCATION_TYPE', models.CharField(blank=True, max_length=70, null=True)),
                ('NAME_FAMILY_STATUS', models.CharField(blank=True, max_length=70, null=True)),
                ('NAME_HOUSING_TYPE', models.CharField(blank=True, max_length=70, null=True)),
                ('OCCUPATION_TYPE', models.CharField(blank=True, max_length=70, null=True)),
                ('WEEKDAY_APPR_PROCESS_START', models.CharField(blank=True, max_length=70, null=True)),
                ('ORGANIZATION_TYPE', models.CharField(blank=True, max_length=70, null=True)),
                ('FONDKAPREMONT_MODE', models.CharField(blank=True, max_length=70, null=True)),
                ('HOUSETYPE_MODE', models.CharField(blank=True, max_length=70, null=True)),
                ('WALLSMATERIAL_MODE', models.CharField(blank=True, max_length=70, null=True)),
                ('EMERGENCYSTATE_MODE', models.CharField(blank=True, max_length=70, null=True)),
                ('TARGET', models.IntegerField(blank=True, null=True)),
                ('CNT_CHILDREN', models.IntegerField(blank=True, null=True)),
                ('AMT_INCOME_TOTAL', models.IntegerField(blank=True, null=True)),
                ('AMT_CREDIT', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('AMT_ANNUITY', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('AMT_GOODS_PRICE', models.IntegerField(blank=True, null=True)),
                ('REGION_POPULATION_RELATIVE', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('DAYS_BIRTH', models.IntegerField(blank=True, null=True)),
                ('DAYS_EMPLOYED', models.IntegerField(blank=True, null=True)),
                ('DAYS_REGISTRATION', models.IntegerField(blank=True, null=True)),
                ('DAYS_ID_PUBLISH', models.IntegerField(blank=True, null=True)),
                ('OWN_CAR_AGE', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('FLAG_MOBIL', models.IntegerField(blank=True, null=True)),
                ('FLAG_EMP_PHONE', models.IntegerField(blank=True, null=True)),
                ('FLAG_WORK_PHONE', models.IntegerField(blank=True, null=True)),
                ('FLAG_CONT_MOBILE', models.IntegerField(blank=True, null=True)),
                ('FLAG_PHONE', models.IntegerField(blank=True, null=True)),
                ('FLAG_EMAIL', models.IntegerField(blank=True, null=True)),
                ('CNT_FAM_MEMBERS', models.IntegerField(blank=True, null=True)),
                ('REGION_RATING_CLIENT', models.IntegerField(blank=True, null=True)),
                ('REGION_RATING_CLIENT_W_CITY', models.IntegerField(blank=True, null=True)),
                ('HOUR_APPR_PROCESS_START', models.IntegerField(blank=True, null=True)),
                ('REG_REGION_NOT_LIVE_REGION', models.IntegerField(blank=True, null=True)),
                ('REG_REGION_NOT_WORK_REGION', models.IntegerField(blank=True, null=True)),
                ('LIVE_REGION_NOT_WORK_REGION', models.IntegerField(blank=True, null=True)),
                ('REG_CITY_NOT_LIVE_CITY', models.IntegerField(blank=True, null=True)),
                ('REG_CITY_NOT_WORK_CITY', models.IntegerField(blank=True, null=True)),
                ('LIVE_CITY_NOT_WORK_CITY', models.IntegerField(blank=True, null=True)),
                ('EXT_SOURCE_1', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('EXT_SOURCE_2', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('EXT_SOURCE_3', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('APARTMENTS_AVG', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('BASEMENTAREA_AVG', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('YEARS_BEGINEXPLUATATION_AVG', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('YEARS_BUILD_AVG', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('COMMONAREA_AVG', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('ELEVATORS_AVG', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('ENTRANCES_AVG', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('FLOORSMAX_AVG', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('FLOORSMIN_AVG', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('LANDAREA_AVG', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('LIVINGAPARTMENTS_AVG', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('LIVINGAREA_AVG', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('NONLIVINGAPARTMENTS_AVG', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('NONLIVINGAREA_AVG', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('APARTMENTS_MODE', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('BASEMENTAREA_MODE', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('YEARS_BEGINEXPLUATATION_MODE', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('YEARS_BUILD_MODE', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('COMMONAREA_MODE', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('ELEVATORS_MODE', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('ENTRANCES_MODE', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('FLOORSMAX_MODE', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('FLOORSMIN_MODE', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('LANDAREA_MODE', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('LIVINGAPARTMENTS_MODE', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('LIVINGAREA_MODE', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('NONLIVINGAPARTMENTS_MODE', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('NONLIVINGAREA_MODE', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('APARTMENTS_MEDI', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('BASEMENTAREA_MEDI', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('YEARS_BEGINEXPLUATATION_MEDI', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('YEARS_BUILD_MEDI', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('COMMONAREA_MEDI', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('ELEVATORS_MEDI', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('ENTRANCES_MEDI', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('FLOORSMAX_MEDI', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('FLOORSMIN_MEDI', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('LANDAREA_MEDI', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('LIVINGAPARTMENTS_MEDI', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('LIVINGAREA_MEDI', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('NONLIVINGAPARTMENTS_MEDI', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('NONLIVINGAREA_MEDI', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('TOTALAREA_MODE', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('OBS_30_CNT_SOCIAL_CIRCLE', models.IntegerField(blank=True, null=True)),
                ('DEF_30_CNT_SOCIAL_CIRCLE', models.IntegerField(blank=True, null=True)),
                ('OBS_60_CNT_SOCIAL_CIRCLE', models.IntegerField(blank=True, null=True)),
                ('DEF_60_CNT_SOCIAL_CIRCLE', models.IntegerField(blank=True, null=True)),
                ('DAYS_LAST_PHONE_CHANGE', models.IntegerField(blank=True, null=True)),
                ('FLAG_DOCUMENT_2', models.IntegerField(blank=True, null=True)),
                ('FLAG_DOCUMENT_3', models.IntegerField(blank=True, null=True)),
                ('FLAG_DOCUMENT_4', models.IntegerField(blank=True, null=True)),
                ('FLAG_DOCUMENT_5', models.IntegerField(blank=True, null=True)),
                ('FLAG_DOCUMENT_6', models.IntegerField(blank=True, null=True)),
                ('FLAG_DOCUMENT_7', models.IntegerField(blank=True, null=True)),
                ('FLAG_DOCUMENT_8', models.IntegerField(blank=True, null=True)),
                ('FLAG_DOCUMENT_9', models.IntegerField(blank=True, null=True)),
                ('FLAG_DOCUMENT_10', models.IntegerField(blank=True, null=True)),
                ('FLAG_DOCUMENT_11', models.IntegerField(blank=True, null=True)),
                ('FLAG_DOCUMENT_12', models.IntegerField(blank=True, null=True)),
                ('FLAG_DOCUMENT_13', models.IntegerField(blank=True, null=True)),
                ('FLAG_DOCUMENT_14', models.IntegerField(blank=True, null=True)),
                ('FLAG_DOCUMENT_15', models.IntegerField(blank=True, null=True)),
                ('FLAG_DOCUMENT_16', models.IntegerField(blank=True, null=True)),
                ('FLAG_DOCUMENT_17', models.IntegerField(blank=True, null=True)),
                ('FLAG_DOCUMENT_18', models.IntegerField(blank=True, null=True)),
                ('FLAG_DOCUMENT_19', models.IntegerField(blank=True, null=True)),
                ('FLAG_DOCUMENT_20', models.IntegerField(blank=True, null=True)),
                ('FLAG_DOCUMENT_21', models.IntegerField(blank=True, null=True)),
                ('AMT_REQ_CREDIT_BUREAU_HOUR', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('AMT_REQ_CREDIT_BUREAU_DAY', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('AMT_REQ_CREDIT_BUREAU_WEEK', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('AMT_REQ_CREDIT_BUREAU_MON', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('AMT_REQ_CREDIT_BUREAU_QRT', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('AMT_REQ_CREDIT_BUREAU_YEAR', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
            ],
        ),
    ]
