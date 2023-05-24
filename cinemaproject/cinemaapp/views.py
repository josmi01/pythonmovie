from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Cinema
from.forms import CinemaForm
# Create your views here.
def index(request):
    cinema=Cinema . objects .all()
    context={
        'cinema_list':cinema
    }
    return render(request,'index.html',context)
def detail(request,cinema_id):
    cinema=Cinema.objects.get(id=cinema_id)
    return render(request,'detail.html',{'cinema':cinema})
def add_cinema(request):
    if request.method=='POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']
        cinema=Cinema(name=name,desc=desc,year=year,img=img)
        cinema.save()
    return render(request,'add.html')
def update(request,id):
    cinema=Cinema.objects.get(id=id)
    form=CinemaForm(request.POST or None,request.FILES,instance=cinema)
    if form. is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'cinema':cinema})
def delete(request,id):
    if request.method=="POST":
        cinema=Cinema.objects.get(id=id)
        cinema.delete()
        return redirect('/')
    return render(request,'delete.html')