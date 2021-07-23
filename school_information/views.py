from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from school_information.forms import Notic_Board_Form
from school_information.models import NoticBoard
# from easy_pdf.views import PDFTemplateView
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    notices = NoticBoard.objects.all()
    context = {"notices":notices}
    return render(request,'school_information/index.html',context)


def notice_details(request,slug,day,month,year):
    notice = NoticBoard.objects.get(slug=slug,added_date__day=day,added_date__month = month,added_date__year=year)
    context = {"notice":notice}
    return render(request,'school_information/notice_details.html',context)

def notice_details(request,slug,day,month,year):
    notice = NoticBoard.objects.get(slug=slug,added_date__day=day,added_date__month = month,added_date__year=year)
    context = {"notice":notice}
    return render(request,'school_information/notice_details.html',context)

    
@login_required
def notice_board(request):
    if request.method == "POST":
        form = Notic_Board_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/school_information/")
    else:
        form = Notic_Board_Form()
    context = {'form':form}
    return render(request,'school_information/notice_board.html',context)

@login_required
def notice_board_edite(request,slug,day,month,year):
    # notice_board = NoticBoard.objects.get(id=id)
    notice_board = NoticBoard.objects.get(slug=slug,added_date__day=day,added_date__month = month,added_date__year=year)
    form = Notic_Board_Form(instance=notice_board)
    if request.method == "POST":
        form = Notic_Board_Form(request.POST,request.FILES,instance=notice_board)
        if form.is_valid():
            form.save()
            return redirect("/school_information/")
    context = {"form":form}
    return render(request,"school_information/notice_board.html",context)

# class notice_details_pdf(PDFTemplateView,DetailView):
#     model = NoticBoard
#     template_name = 'school_information/notice_details.html'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['']