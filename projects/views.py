from django.shortcuts import render
from .models import Project

# Create your views here.
def showprojects(request):
    projectdata=Project.objects.all()
    context={
        'projects' :projectdata
    }
    return render(request, "projects/proj.html",context)

def project_detail(request,pk):
    project_detail=Project.objects.get(pk=pk)
    context={
        'project' : project_detail
    }
    return render(request,'projects/projectdetails.html',context)