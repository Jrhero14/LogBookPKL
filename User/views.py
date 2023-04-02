from django.shortcuts import render, redirect
from .models import Log
import datetime

# Utils Function
def newLog(request):
    print(request.POST)
    new = Log(
        dateLog=datetime.datetime.strptime(request.POST['Date'], '%Y-%m-%d').date(),
        logDiary=request.POST['Log']
    )
    new.save()
    return redirect('/')

# Create your views here.
def indexViews(request):
    dataLog = Log.objects.all().order_by('-id')
    contexts = {
        'logData': dataLog
    }
    return render(request, 'index.html', context=contexts)