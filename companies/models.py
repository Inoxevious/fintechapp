from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class  LoanApplication(models.Model):
    SK_ID_CURR = models.IntegerField(null=True ,blank=True)
    TARGET = models.IntegerField(null=True ,blank=True)
    NAME_CONTRACT_TYPE = models.CharField(null=True ,blank=True,max_length=70)
    CODE_GENDER = models.CharField(null=True ,blank=True,max_length=70)
    FLAG_OWN_CAR = models.CharField(null=True ,blank=True,max_length=70)
    FLAG_OWN_REALTY = models.CharField(null=True ,blank=True,max_length=70)
    CNT_CHILDREN = models.IntegerField(null=True ,blank=True)
    AMT_INCOME_TOTAL = models.DecimalField(max_digits=15,decimal_places=5,null=True ,blank=True)
    AMT_CREDIT = models.DecimalField(max_digits=15,decimal_places=5,null=True ,blank=True)
    AMT_ANNUITY = models.DecimalField(max_digits=15,decimal_places=5,null=True ,blank=True)
    AMT_GOODS_PRICE = models.IntegerField(null=True ,blank=True)
    NAME_TYPE_SUITE = models.CharField(null=True ,blank=True,max_length=70)
    NAME_INCOME_TYPE = models.CharField(null=True ,blank=True,max_length=70)
    NAME_EDUCATION_TYPE = models.CharField(null=True ,blank=True,max_length=70)
    NAME_FAMILY_STATUS = models.CharField(null=True ,blank=True,max_length=70)
    NAME_HOUSING_TYPE = models.CharField(null=True ,blank=True,max_length=70)
    REGION_POPULATION_RELATIVE = models.DecimalField(max_digits=15,decimal_places=5,null=True ,blank=True)
    DAYS_BIRTH = models.IntegerField(null=True ,blank=True)
    DAYS_EMPLOYED = models.IntegerField(null=True ,blank=True)
    DAYS_REGISTRATION = models.IntegerField(null=True ,blank=True)
    DAYS_ID_PUBLISH = models.IntegerField(null=True ,blank=True)
    OWN_CAR_AGE = models.IntegerField(null=True ,blank=True)
    FLAG_MOBIL = models.IntegerField(null=True ,blank=True)
    FLAG_EMP_PHONE = models.IntegerField(null=True ,blank=True)
    FLAG_WORK_PHONE = models.IntegerField(null=True ,blank=True)
    FLAG_CONT_MOBILE = models.IntegerField(null=True ,blank=True)
    FLAG_PHONE = models.IntegerField(null=True ,blank=True)
    FLAG_EMAIL = models.IntegerField(null=True ,blank=True)
    OCCUPATION_TYPE = models.CharField(null=True ,blank=True,max_length=70)
    CNT_FAM_MEMBERS = models.IntegerField(null=True ,blank=True)
    REGION_RATING_CLIENT = models.IntegerField(null=True ,blank=True)
    REGION_RATING_CLIENT_W_CITY = models.IntegerField(null=True ,blank=True)
    WEEKDAY_APPR_PROCESS_START = models.CharField(null=True ,blank=True,max_length=70)
    HOUR_APPR_PROCESS_START = models.IntegerField(null=True ,blank=True)
    REG_REGION_NOT_LIVE_REGION = models.IntegerField(null=True ,blank=True)
    REG_REGION_NOT_WORK_REGION = models.IntegerField(null=True ,blank=True)
    LIVE_REGION_NOT_WORK_REGION = models.IntegerField(null=True ,blank=True)
    REG_CITY_NOT_LIVE_CITY = models.IntegerField(null=True ,blank=True)
    REG_CITY_NOT_WORK_CITY = models.IntegerField(null=True ,blank=True)
    LIVE_CITY_NOT_WORK_CITY = models.IntegerField(null=True ,blank=True)
    ORGANIZATION_TYPE = models.CharField(null=True ,blank=True,max_length=70)
    EXT_SOURCE_1 = models.DecimalField(max_digits=15,decimal_places=5,null=True ,blank=True)
    EXT_SOURCE_2 = models.DecimalField(max_digits=15,decimal_places=5,null=True ,blank=True)
    EXT_SOURCE_3 = models.DecimalField(max_digits=15,decimal_places=5,null=True ,blank=True)
    APARTMENTS_AVG = models.DecimalField(max_digits=15,decimal_places=5,null=True ,blank=True)
    BASEMENTAREA_AVG = models.DecimalField(max_digits=15,decimal_places=5,null=True ,blank=True)
    YEARS_BEGINEXPLUATATION_AVG = models.DecimalField(max_digits=15,decimal_places=5,null=True ,blank=True)
    YEARS_BUILD_AVG = models.DecimalField(max_digits=15,decimal_places=5,null=True ,blank=True)
    COMMONAREA_AVG = models.DecimalField(max_digits=15,decimal_places=5,null=True ,blank=True)
    ELEVATORS_AVG = models.DecimalField(max_digits=15,decimal_places=5,null=True ,blank=True)
    ENTRANCES_AVG = models.DecimalField(max_digits=15,decimal_places=5,null=True ,blank=True)
    FLOORSMAX_AVG = models.DecimalField(max_digits=15,decimal_places=5,null=True ,blank=True)
    FLOORSMIN_AVG = models.DecimalField(max_digits=15,decimal_places=5,null=True ,blank=True)
    LANDAREA_AVG = models.DecimalField(max_digits=15,decimal_places=5,null=True ,blank=True)
    LIVINGAPARTMENTS_AVG = models.DecimalField(max_digits=15,decimal_places=5,null=True ,blank=True)
    LIVINGAREA_AVG = models.DecimalField(max_digits=15,decimal_places=5,null=True ,blank=True)
    NONLIVINGAPARTMENTS_AVG = models.DecimalField(max_digits=15,decimal_places=5,null=True ,blank=True)
    NONLIVINGAREA_AVG = models.DecimalField(max_digits=15,decimal_places=5,null=True ,blank=True)
    APARTMENTS_MODE = models.DecimalField(max_digits=15,decimal_places=5,null=True ,blank=True)
    BASEMENTAREA_MODE = models.DecimalField(max_digits=15,decimal_places=5,null=True ,blank=True)
    YEARS_BEGINEXPLUATATION_MODE = models.DecimalField(max_digits=15,decimal_places=5,null=True ,blank=True)
    YEARS_BUILD_MODE = models.DecimalField(max_digits=15,decimal_places=5,null=True ,blank=True)
    COMMONAREA_MODE = models.DecimalField(max_digits=15,decimal_places=5,null=True ,blank=True)
    ELEVATORS_MODE = models.DecimalField(max_digits=15,decimal_places=5,null=True ,blank=True)
    ENTRANCES_MODE = models.DecimalField(max_digits=15,decimal_places=5,null=True ,blank=True)
    FLOORSMAX_MODE = models.DecimalField(max_digits=15,decimal_places=5,null=True ,blank=True)
    FLOORSMIN_MODE = models.DecimalField(max_digits=15,decimal_places=5,null=True ,blank=True)
    LANDAREA_MODE = models.DecimalField(max_digits=15,decimal_places=5,null=True ,blank=True)
    LIVINGAPARTMENTS_MODE = models.DecimalField(max_digits=15,decimal_places=5,null=True ,blank=True)
    LIVINGAREA_MODE = models.DecimalField(max_digits=15,decimal_places=5,null=True ,blank=True)
    NONLIVINGAPARTMENTS_MODE = models.DecimalField(max_digits=15,decimal_places=5,null=True ,blank=True)
    NONLIVINGAREA_MODE = models.DecimalField(max_digits=15,decimal_places=5,null=True ,blank=True)
    APARTMENTS_MEDI = models.DecimalField(max_digits=15,decimal_places=5,null=True ,blank=True)
    BASEMENTAREA_MEDI = models.DecimalField(max_digits=15,decimal_places=5,null=True ,blank=True)
    YEARS_BEGINEXPLUATATION_MEDI = models.DecimalField(max_digits=15,decimal_places=5,null=True ,blank=True)
    YEARS_BUILD_MEDI = models.DecimalField(max_digits=15,decimal_places=5,null=True ,blank=True)
    COMMONAREA_MEDI = models.DecimalField(max_digits=15,decimal_places=5,null=True ,blank=True)
    ELEVATORS_MEDI = models.DecimalField(max_digits=15,decimal_places=5,null=True ,blank=True)
    ENTRANCES_MEDI = models.DecimalField(max_digits=15,decimal_places=5,null=True ,blank=True)
    FLOORSMAX_MEDI = models.DecimalField(max_digits=15,decimal_places=5,null=True ,blank=True)
    FLOORSMIN_MEDI = models.DecimalField(max_digits=15,decimal_places=5,null=True ,blank=True)
    LANDAREA_MEDI = models.DecimalField(max_digits=15,decimal_places=5,null=True ,blank=True)
    LIVINGAPARTMENTS_MEDI = models.DecimalField(max_digits=15,decimal_places=5,null=True ,blank=True)
    LIVINGAREA_MEDI = models.DecimalField(max_digits=15,decimal_places=5,null=True ,blank=True)
    NONLIVINGAPARTMENTS_MEDI = models.DecimalField(max_digits=15,decimal_places=5,null=True ,blank=True)
    NONLIVINGAREA_MEDI = models.DecimalField(max_digits=15,decimal_places=5,null=True ,blank=True)
    FONDKAPREMONT_MODE = models.CharField(null=True ,blank=True,max_length=70)
    HOUSETYPE_MODE = models.CharField(null=True ,blank=True,max_length=70)
    TOTALAREA_MODE = models.DecimalField(max_digits=15,decimal_places=5,null=True ,blank=True)
    WALLSMATERIAL_MODE = models.CharField(null=True ,blank=True,max_length=70)
    EMERGENCYSTATE_MODE = models.CharField(null=True ,blank=True,max_length=70)
    OBS_30_CNT_SOCIAL_CIRCLE = models.IntegerField(null=True ,blank=True)
    DEF_30_CNT_SOCIAL_CIRCLE = models.IntegerField(null=True ,blank=True)
    OBS_60_CNT_SOCIAL_CIRCLE = models.IntegerField(null=True ,blank=True)
    DEF_60_CNT_SOCIAL_CIRCLE = models.IntegerField(null=True ,blank=True)
    DAYS_LAST_PHONE_CHANGE = models.IntegerField(null=True ,blank=True)
    FLAG_DOCUMENT_2 = models.IntegerField(null=True ,blank=True)
    def __str__(self):
        return self.SK_ID_CURR

class Role(models.Model):
    owner = 'owner'
    officer = 'officer'
    manager = 'manager'
    admin = 'admin'
    executive = 'executive'
    client = 'client'
    field_officer = 'field_officer'
    internal_officer = 'internal_officer'
    USER_GROUP_CHOICES = [
            (client,'client'),
            (executive,'executive'),
            (field_officer,'field_officer'),
            (internal_officer,'internal_officer'),
        ]

    ROLE_CHOICES = [
            (client,'client'),
            (owner,'owner'),
            (officer,'officer'),
            (manager,'manager'),
            (admin,'admin'),
        ]
    name = models.CharField(max_length=70, choices=ROLE_CHOICES, default = officer)
    user_group = models.CharField(max_length=70, choices=USER_GROUP_CHOICES, default = field_officer)

    def __str__(self):
        return self.name

class Country(models.Model): 
    name = models.CharField(max_length=200, default='zim')
    official_language = models.TextField(null=True ,blank=True)
    flag = models.ImageField(null=True ,blank=True, upload_to='static/images/countries/flags')
    longi = models.TextField(null=True ,blank=True)
    lat = models.TextField(null=True ,blank=True) 

class Organization(models.Model):
    owner = models.ForeignKey(User, related_name="organization", verbose_name="Micro Finance Director", on_delete = models.CASCADE)
    business_name = models.CharField(max_length=70,null=True ,blank=True)
    business_trading_name = models.CharField(max_length=70,null=True ,blank=True)
    registered_byuser_as = models.ForeignKey(Role, verbose_name="Admin", on_delete = models.CASCADE,null=True ,blank=True)
    total_branches =models.IntegerField(null=True ,blank=True)
    profile_pic = models.ImageField(null=True ,blank=True, upload_to='staticfiles/images')
    address =models.TextField(null=True ,blank=True)
    phone =models.CharField(null=True ,blank=True,max_length=70)
    logo = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    icon = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    image1 = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    statement =models.TextField(null=True ,blank=True)
    acceptPush = models.BooleanField(default=False)
    pushToken = models.CharField(max_length=100, null=True, blank=True,db_index=True)
    is_active = models.BooleanField(('active'), default=True)

    def __str__(self):
        return self.business_name

class Department(models.Model):
    organization =  models.ForeignKey(Organization, related_name="department", verbose_name="Department", on_delete=models.CASCADE, default=0)
    name = models.CharField(null=True ,blank=True,max_length=20)
    head = models.OneToOneField(User, on_delete = models.CASCADE)
    mission =models.TextField(null=True ,blank=True)
    vision =models.TextField(null=True ,blank=True)
    statement =models.TextField(null=True ,blank=True)
    image = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    video = models.FileField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    def __str__(self):
        return self.name


