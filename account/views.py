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


# Create your views here.
# 


@login_required(login_url='/pages/login/')
def index(request, **kwargs):
        owner = "owner"
        admin ="admin"
        officer = "officer"
        manager = "manager"
        user_url = ''

        user_id = request.user.id
        account_user = AccountUser.objects.get(user_id=user_id)
 

        if str(account_user.role) == admin:
            user_url = 'admin' 

        elif str(account_user.role) == owner:
            user_url = 'owner'
                   
        elif str(account_user.role) == officer:
            user_url = 'officer'
          
        elif str(account_user.role) == manager:
            user_url = 'manager'
        else:
            user_url = 'pages/login.html'
        
        return HttpResponseRedirect(reverse(user_url, kwargs={'user_id': user_id }))


def login(request):
    if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']

       user = auth.authenticate(username = username,password = password)

       if user:

           auth.login(request,user)
           messages.success(request,"You are now logged in.")
           return redirect('account:index')

          
       else:
            messages.error(request,"Invalid Credentials")
            return redirect('login')       
    else:
        return render(request,'pages/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,"Logged Out")
    return redirect('index')

def register(request):
    
    if request.method == "POST":
        
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        try:
            role = request.POST['role']
        except MultiValueDictKeyError:
            role = 'undefined'

       

        # Check if passwords match
        if password == password2:
            # Check username
            if User.objects.filter(username = username).exists():
                messages.error(request,"That username is taken.")
                return redirect('pages/register')
            else:
                if User.objects.filter(email = email).exists():
                    messages.error(request,"That email is taken.")
                    return redirect('pages/register')
                else:
                    # looks good
                    
                    user = User.objects.create_user(username = username,
                    password = password,email=email,first_name = first_name,
                    last_name = last_name )
                    user.save()

                    user = get_object_or_404(User, email = email)  
                    acc = AccountUser(user_id = user.id, role = role)          
                    acc.save()
                    # Login after register
                    auth.login(request,user)
                    messages.success(request,"You are now registered in.")
                    return redirect('login')

                    # # Login manually 
                    # messages.success(request,"You can now log in.")
                    # return redirect('login')
        else:
            messages.error(request,'Passwords do not match.')
            return redirect('pages/register')
    else:
        context = {
            'role_choices': role_choices,
           
        }
        return render(request,'pages/register.html' , context)

def account_activation_sent(request):

    return render(request, 'registration/account_activation_sent.html')

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
                return render(request,'home.html')
            else:
                return render(request, 'registration/account_activation_invalid.html')

    else:
        form = DelegationForm()
    return render(request, 'registration/delegation.html', {'form': form})



