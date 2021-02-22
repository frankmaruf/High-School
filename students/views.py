from django.shortcuts import render,HttpResponse,reverse,redirect, get_object_or_404, get_list_or_404
from students.forms import StudentsForm,EditStudentForm
from students.models import Students
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from school_information.models import Department,Subject
# Create your views here.

def index(request):
    students = Students.objects.order_by("-roll").all()
    return render(request,'students/index.html',context={'students':students})

def student_detail(request,certificate):
    student = get_object_or_404(Students, birth_certificate = certificate)
    return render(request,'students/details.html',context={"student":student})



def StudentsAdd(request):
    form = StudentsForm()
    if request.method == 'POST':
        form = StudentsForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            if "profile_pic" in request.FILES:
                student.profile_pic = request.FILES['profile_pic']
            student.save()
            messages.success(request, ("You have Registered a Students.."))
            return redirect('/')
    else:
        form = StudentsForm()
    return render(request,'students/students_add.html',context={'form':form})


@login_required
def EditStudent(request,certificate):
    student = Students.objects.get(birth_certificate=certificate)
    form = EditStudentForm(instance=student)
    if request.method == 'POST':
        form = EditStudentForm(request.POST,instance=student)
        if form.is_valid():
            student = form.save(commit=False)
            if "profile_pic" in request.FILES:
                student.profile_pic = request.FILES['profile_pic']
            student.save()
            messages.success(request, ("You have Update a Students.."))
            return redirect('/')
    context = {'form':form}
    return render(request,'students/students_add.html',context)
