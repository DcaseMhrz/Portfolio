from django.shortcuts import render

# Create your views here.
def showcontacts(request):
    return render(request,'contact/contactpage.html',{})
