from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect

# Create your views here.
from crudapp.form import todoform
from crudapp.models import task


def add(request):


    TASK1 = task.objects.all()
    if request.method=='POST':
         name=request.POST.get('name','')
         priority=request.POST.get('priority','')
         date=request.POST.get('date','')
         TASK=task(name=name,priority=priority,date=date)
         TASK.save()
    paginator = Paginator(TASK1, 3)
    try:
         page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
      products = paginator.page(page)
    except (EmptyPage, InvalidPage):
             products = paginator.page(paginator.num_pages)
             return redirect('/')
    return render(request,'home.html',{'TASK1':TASK1,'products':products })
# def details(request):

    # return render(request,'details.html',)
def delete(request,taskid):
    task11=task.objects.get(id=taskid)
    if request.method=='POST':
        task11.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    TASK=task.objects.get(id=id)
    f=todoform(request.POST or None, instance=TASK)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'TASK':TASK})