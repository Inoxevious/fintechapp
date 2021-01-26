from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal as D
from companies.models import Organization, Department, Role
# Create your models here.
class AccountUser(models.Model):

    user = models.OneToOneField(User, related_name="account_user", verbose_name="Account User", on_delete = models.CASCADE)
    organization =  models.ForeignKey(Organization, on_delete=models.CASCADE, default=0)
    department =  models.ForeignKey(Department, on_delete=models.CASCADE, default=0)
    role =  models.ForeignKey(Role, on_delete=models.CASCADE, default=0)
    category = models.CharField(null=True ,blank=True,max_length=70)
    age = models.IntegerField(null=True ,blank=True)
    email_confirmed = models.BooleanField(default=False)
    address =models.TextField(null=True ,blank=True)
    date_birth =models.DateField(null=True ,blank=True)
    phone =models.CharField(null=True ,blank=True,max_length=70)
    id_number =models.CharField(null=True ,blank=True,max_length=20)
    gender =models.CharField(null=True ,blank=True,max_length=20)
    education_level =models.CharField(null=True ,blank=True,max_length=70)
    marital_status =models.CharField(null=True ,blank=True,max_length=20)
    number_dependants =models.IntegerField(null=True ,blank=True)
    total_worth =models.IntegerField(null=True ,blank=True)
    profile_pic = models.ImageField(null=True ,blank=True, upload_to='staticfiles/images')
    facebookId = models.CharField(max_length=100, null=True, blank=True,db_index=True)
    android = models.BooleanField(blank=True, default=False)
    ios = models.NullBooleanField(blank=True, default=False, null=True)
    acceptPush = models.BooleanField(default=False)
    pushToken = models.CharField(max_length=100, null=True, blank=True,db_index=True)
    is_active = models.BooleanField(('active'), default=True)

    def __str__(self):
        return self.user.username


class About_us(models.Model):
    org = models.ForeignKey(Organization, related_name="about_us", verbose_name="About Us", on_delete = models.CASCADE,null=True, blank=True)
    tag_text =models.CharField(max_length=50,null=True ,blank=True)
    logo = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    icon = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    image1 = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    image2 = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    image3 = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    image4 = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    video = models.FileField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    statement =models.TextField(null=True ,blank=True)
    statement2 =models.TextField(null=True ,blank=True)
    statement3 =models.TextField(null=True ,blank=True)
    isActive = models.BooleanField(default=True)
    isFaceBanner = models.BooleanField(default=False)
    written_date = models.DateTimeField()
    published_date = models.DateTimeField()
    expire_date = models.DateTimeField()

    def __str__(self):
        return self.tag_text

class LoanOfficer(models.Model):
    info = models.ForeignKey(AccountUser, related_name="officer", verbose_name="About Us", on_delete = models.CASCADE,null=True, blank=True)
    insti = models.ForeignKey(Organization, on_delete = models.CASCADE,null=True, blank=True)
    signup_date = models.DateTimeField()
    def __str__(self):
        return self.info.user.username
class Clients(models.Model):
    info = models.ForeignKey(AccountUser, related_name="client", verbose_name="Client", on_delete = models.CASCADE,null=True, blank=True)
    insti = models.ForeignKey(Organization, on_delete = models.CASCADE,null=True, blank=True)
    signing_officer = models.ForeignKey(LoanOfficer, related_name="client_account_officer", verbose_name="Account Officer", on_delete = models.CASCADE,null=True, blank=True)
    registration_date = models.DateTimeField()
    def __str__(self):
        return self.info.user.username

class Loan(models.Model):
    signing_officer = models.ForeignKey(LoanOfficer, related_name="loan_officer", verbose_name="Account Officer", on_delete = models.CASCADE,null=True, blank=True)
    client = models.ForeignKey(AccountUser, related_name="loan_client", verbose_name="Client", on_delete = models.CASCADE,null=True, blank=True)
    application_date = models.DateTimeField()
    approval_date = models.DateTimeField()
    loan_term =models.CharField(null=True ,blank=True,max_length=20)
    colleteral = models.CharField(null=True ,blank=True,max_length=20)
    amount= models.CharField(null=True ,blank=True,max_length=20)
    def __str__(self):
        return self.client.user.username