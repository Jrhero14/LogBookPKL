from django.shortcuts import render, redirect
from .models import Log
import datetime

# Utils Function
def newLog(request):
    new = Log(
        dateLog=datetime.datetime.strptime(request.POST['Date'], '%Y-%m-%d').date(),
        logDiary=request.POST['Log']
    )
    new.save()
    return redirect('/')

def editLog(request):
    edit = Log.objects.get(id=request.POST['edit-log-id'])
    edit.dateLog = datetime.datetime.strptime(request.POST['tanggal-edit'], '%Y-%m-%d').date()
    edit.logDiary = request.POST['log-edit']
    edit.save()
    return redirect('/')

def deleteLogBook(request):
    log = Log.objects.get(id=request.POST['delete-id'])
    log.delete()
    return redirect('/')

# Create your views here.
def indexViews(request):
    dataLog = Log.objects.all().order_by('-id')
    contexts = {
        'logData': dataLog
    }
    return render(request, 'index.html', context=contexts)