from .models import AccountUser
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.contrib import messages, auth
from .choices import state_choices, role_choices
from django.utils.datastructures import MultiValueDictKeyError
from companies.models import Organization, Role, Department
from datetime import datetime, date
# Create your views here.
# 
def home(request):
    return render(request,'account/auth/login.html')

@login_required(login_url='/account/login/')
def index(request, **kwargs):
        owner = "owner"
        admin ="admin"
        officer = "officer"
        manager = "manager"
        user_url = ''

        user_id = request.user.id
        print("User ID", user_id)
        if AccountUser.objects.filter(user_id=user_id).exists():
            account_user = AccountUser.objects.get(user_id=user_id)
        else:
            messages.success(request,"Hie Admin, {} You not authorised to analytics dashboards, use admin portal.".format(user.username))
            return redirect('account:login')

        request.session['account_user_id'] = account_user.id
        print("account_user ID", account_user)
        context ={
            'account_user':account_user
        }

        if str(account_user.role) == officer or str(account_user.role) == manager:
            user_url = 'companies:index' 

        # elif str(account_user.role) == owner:
        #     user_url = 'companies'
                   
        # elif str(account_user.role) == officer:
        #     user_url = 'companies'
          
        # elif str(account_user.role) == manager:
        #     user_url = 'companies'
        # else:
        #     user_url = 'account:login'
        # return render(request, "dashboards/landing/index.html", context)
        return HttpResponseRedirect(reverse(user_url, kwargs={'user_id': user_id }))


def login(request):
    if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']

       user = auth.authenticate(username = username,password = password)

       if user:

           auth.login(request,user)
           
           return redirect('account:index')

          
       else:
            messages.error(request,"Invalid Credentials")
            return redirect('account:login')       
    else:
        return render(request,'account/auth/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,"Logged Out")
    return redirect('account:home')

def register(request):
    role_choices = Role.objects.all()
    context = {
        'role_choices': role_choices,
        
    }
    if request.method == "POST":
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        work_email = request.POST['work_email']
        personal_email = request.POST['personal_email']
        password = request.POST['password1']
        password2 = request.POST['password2']
        business_name = request.POST['business_name']
        business_trading_name = request.POST['business_trading_name']
        total_branches = request.POST['total_branches']
        terms = request.POST['terms']
        username = personal_email


        try:
            role = request.POST['role']
            if role == 'manager':
                role_ins = Role.objects.get(name=role)
            else:
                role_ins = Role.objects.get(id=role)
        except MultiValueDictKeyError:
            role = 'undefined'
        try:
            last_name = request.POST['last_name']
        except MultiValueDictKeyError:
            last_name = 'undefined'
        # Check if passwords match
        if password == password2:
            # Check username
            if User.objects.filter(username = username).exists():
                messages.error(request,"That username is taken.")
                return redirect('account:register')
            else:
                if User.objects.filter(email = personal_email).exists():
                    messages.error(request,"That email is taken.")
                    return redirect('account:register')
                else:
                        # looks good
                    print("USER ADDED")
                    user = User.objects.create_user(username = personal_email,
                    password = password,email=personal_email,first_name = first_name,
                    last_name = last_name )
                    user.save()
                    if user.id:
                        org = Organization(
                                owner = user, business_name = business_name, 
                                business_trading_name = business_trading_name, 
                                registered_byuser_as = role_ins, total_branches = total_branches
                        )
                        org.save()
                        if org.id:
                            acc = AccountUser(user = user, role = role_ins, personal_email=personal_email, organization=org, work_email=work_email)          
                            acc.save()
                            if acc.id:
                                messages.success(request,"Welcom, {} You are now registered with Fintech.".format(user.first_name))
                                return redirect('account:login')
                            else:
                                messages.error(request,'Could not create business account')
                                return redirect('account:register')

                    # # Login manually 
                    # messages.success(request,"You can now log in.")
                    # return redirect('login')
        else:
            messages.error(request,'Passwords do not match.')
            return redirect('account:register')
    else:

        return render(request,'account/auth/registration.html' , context)

    return render(request,'account/auth/registration.html' , context)

def account_activation_sent(request):

    return render(request, 'account/auth/registration/account_activation_sent.html')

def activate(request, uidb64, token):
    form = DelegationForm(request.POST)
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if request.method == 'POST':
        
        if form.is_valid():
            if user is not None and account_activation_token.check_token(user, token):
                user.is_active = True
                user.accountuser.email_confirmed = True
                user.accountuser.country = form.cleaned_data.get('country')
                user.accountuser.role = form.cleaned_data.get('role')
                user.save()
                login(request, user)
                return render(request,'account/index.html')
            else:
                return render(request, 'account/auth/registration/account_activation_invalid.html')

    else:
        form = DelegationForm()
    return render(request, 'registration/auth/delegation.html', {'form': form})

def view_client(request,loan_id):
     return render(request,'dashboards/clients/profile/index.html')