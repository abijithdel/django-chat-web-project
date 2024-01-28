from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login  as auth_login 
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash



# Create your views here.

def login(req):
    if req.method == 'POST':
        uname = req.POST.get('username')
        pas = req.POST.get('password')
        user = authenticate(req,username=uname,password=pas)
        if user is not None:
            auth_login(req,user)
            welcom = 'congratulations.successfully logged in'
            return render(req,'home.html',{'welcom':welcom})
        else:
            us_pas_not_mach='CHECK YOUR USERNAME''AND CHECK YOUR PASSWORD'
            return render(req,'accout/login.html',{'us_pas_not_mach':us_pas_not_mach})

    return render(req,'accout/login.html')

def sigup(req):
    if req.method == 'POST':
        fname = req.POST.get('fname')
        lname = req.POST.get('lname')
        uname = req.POST.get('username')
        email = req.POST.get('email')
        pass1 = req.POST.get('password')
        pass2 = req.POST.get('password2')
        
        if pass1 != pass2:
            pass_not_mach='CHECK YOUR PASSWORD AND CONFORM PASSWORD'
            return render(req,'accout/signup.html',{'pass_not_mach':pass_not_mach})
        

        elif User.objects.filter(username=uname).exists():
            username_taken = 'Username already taken'
            return render(req, 'accout/signup.html', {'username_taken': username_taken})
        else:
            
                
            users = User.objects.create_user(username=uname, email=email, password=pass1, first_name=fname, last_name=lname)
            users.save()
            wel_mess='hello',fname
            return render(req,'home.html',{'wel_mess':wel_mess})
            
    return render(req,'accout/signup.html')

@login_required(login_url='login')
def accout(req):
    return render(req,'accout/accout.html')

def logot(req):
    logout(req)
    return render(req,'accout/login.html')


def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()
        saccessf = 'Profile saccessfully Edited'
        return render(request, 'accout/accout.html', {'user': user , "saccess":saccessf})
    return render(request, 'accout/edit_profile.html', {'user': user})

def reset_pass(req):
    user = req.user
    if req.method == 'POST':
        pass1 = req.POST.get('newpass')
        pass2 = req.POST.get('cpass')
        if pass1 != pass2:
            response ="Check Conform Password"
            return render(req,'accout/newpass.html',{'response':response})

        else:
          user.set_password(pass1)
          update_session_auth_hash(req, user)
          user.save()
          responses = "Password Changed"
          return render(req,'accout/accout.html',{'responses':responses})
    return render(req,'accout/newpass.html')

def delete_accout_user(req):
    if req.method == 'POST':
        user = req.user
        user.delete()
        alert = 'Your Accout Deleted'
        return render(req,'accout/signup.html',{'alert':alert})
    return render(req,'accout/ac_delete.html')