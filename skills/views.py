from django.shortcuts import render

import skills



from .models import Skill

# Create your views here.
def showskills(request):
    data=Skill.objects.all().values()
    context={
        'sname': data
    }
    return render(request,'skills/skills.html',context)