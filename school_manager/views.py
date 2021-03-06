from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib import messages
from school_manager.forms import SignUpForm,CustomUserProfileInfoCreationForm,EditeProfileForm
from django.utils.translation import gettext_lazy as _
from django.db import transaction
from django.contrib.auth.models import User
from school_manager.models import UserProfileInfo
from school_manager.decorators import unauthenticated_user
# Create your views here.


def manager_list(request):
    user = User.objects.all()
    context = {'managers':user}
    return render(request,'school_manager/manager_list.html',context)

def manager_profile(request,username):
    user = User.objects.get(username=username)
    context = {'user':user}
    return render(request,'school_manager/manager_profile.html',context)

@unauthenticated_user
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,("You have Been Logged In!"))
            return redirect('/school_manager/')
            # Redirect to a success page.
        else:
            messages.success(request,("Error Loggin in - Please Try Again.."))
            return redirect('login')
    else:   # Return an 'invalid login' error message.
        return render(request,"authenticate/login.html")

@login_required
def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged Out..."))
    return redirect('/')

@unauthenticated_user
def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        extra_info = CustomUserProfileInfoCreationForm(request.POST)

        if form.is_valid() and extra_info.is_valid():
            user = form.save()
            profile = extra_info.save(commit=False)
            if "profile_pic" in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.user = user
            profile.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request,username = username,password = password)
            login(request,user)
            messages.success(request,("You have Registered.."))
            return redirect('/school_manager/')

    else:
        form = SignUpForm()
        extra_info = CustomUserProfileInfoCreationForm()
    context = {'form': form,'extra_info':extra_info}
    return render(request,'authenticate/register.html',context)





@login_required
@transaction.atomic
def edit_prifile(request):
    if request.method == "POST":
        form = EditeProfileForm(request.POST, instance=request.user)
        extra_info = CustomUserProfileInfoCreationForm(request.POST, instance=request.user.userprofileinfouser)

        if form.is_valid() and extra_info.is_valid():
            user = form.save()
            profile = extra_info.save(commit=False)
            if "profile_pic" in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.user = user
            profile.save()
            messages.success(request,("Your profile was successfully updated!"))
            return redirect('/school_manager/')
        else:
            messages.error(request, _('Please correct the error below.'))

    else:
        form = EditeProfileForm(instance=request.user)
        extra_info = CustomUserProfileInfoCreationForm(instance=request.user.userprofileinfo)
    context = {'form': form,'extra_info':extra_info}
    return render(request,'school_manager/edit_profile.html',context)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request,("You have Edited Your Password.."))
            return redirect('/school_manager/')
    else:
        form = PasswordChangeForm(user=request.user)
    context = {'form':form}
    return render(request,'school_manager/change_password.html',context)


