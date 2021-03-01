from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from teachers.models import Teachers
from teachers.forms import TeachersForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    teachers = Teachers.objects.all()
    context = {"teachers":teachers}
    return render(request,'teachers/index.html',context)

def teachers_profile(request,certificate):
    teachers = get_object_or_404(Teachers,birth_certificate=certificate)
    context = {'teachers':teachers}
    return render(request,'teachers/profile.html',context)

@login_required
def TeachersAdd(request):
    form = TeachersForm()
    if request.method == 'POST':
        form = TeachersForm(request.POST)
        if form.is_valid():
            teacher = form.save(commit=False)
            if 'profile_pic' in request.FILES:
                teacher.profile_pic = request.FILES['profile_pic']
            teacher.save()
            form.save_m2m()
            return redirect('/teachers')
    else:
        form = TeachersForm()
    context = {'form':form}
    return render(request,'teachers/teachers_add.html',context)
    
@login_required
def EditTeacher(request,certificate):
    teacher = Teachers.objects.get(birth_certificate=certificate)
    form = TeachersForm(instance=teacher)
    if request.method == 'POST':
        form = TeachersForm(request.POST,instance=teacher)
        if form.is_valid():
            teacher = form.save(commit=False)
            if 'profile_pic' in request.FILES:
                teacher.profile_pic = request.FILES['profile_pic']
            teacher.save()
            form.save_m2m()
            return redirect('/teachers')
    context = {'form':form}
    return render(request,'teachers/teachers_add.html',context)