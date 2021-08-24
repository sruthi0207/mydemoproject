from urllib import request

from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.p
from restapp.models import Rest
from .forms import RestForm
from . models import Rest

def index(request):
    rest = Rest.objects.all()
    return render(request,'index.html',{'plist': rest})

def detail(request,rest_id):
    rest=Rest.objects.get(id=rest_id)
    return render(request,"detail.html",{'rest':rest})

def addfood(request):
        if request.method == "POST":
            n1 = request.POST.get('name', )
            n2 = request.POST.get('desc', )
            n3 = request.POST.get('flavour', )
            img = request.FILES['img']
            food=Rest(name=n1, desc=n2,flavour=n3, img=img)
            food.save()
            # return HttpResponse("Food item added")
            return redirect('/')
        else:
            return render(request,'addfood.html')
def update(request,id):
    rest= Rest.objects.get(id=id)
    form=RestForm(request.POST or None,request.FILES,instance=rest)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'rest':rest})
def delete(request,id):
    if request.method=='POST':
        movie = Rest.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')
