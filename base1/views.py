from django.shortcuts import render

# Create your views here.
def Home(request):
    a="D jango"
    b="Base"
    context={
        'user':a,
        'pl':b
    }
    return render(request,'basejango.html',context)

def Log(request):
    return render(request,'basejango1.html')