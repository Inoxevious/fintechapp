from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Country(models.Model): 
    name = models.CharField(max_length=200, default='zim')
    official_language = models.TextField(null=True ,blank=True)
    flag = models.ImageField(null=True ,blank=True, upload_to='static/images/countries/flags')
    longi = models.TextField(null=True ,blank=True)
    lat = models.TextField(null=True ,blank=True) 

class Organization(models.Model):
    owner = models.ForeignKey(User, related_name="organization", verbose_name="Micro Finance Director", on_delete = models.CASCADE)
    name = models.CharField(max_length=70)
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
        return self.name

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