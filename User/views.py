from django.shortcuts import render, redirect
from .models import Log, imgDoc
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
import datetime, os, json

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

# Utils Function
def handle_uploaded_file(f, dir):
    with open(f"./static/images/documentation/{dir}/{f.name}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def dir_documentation(dirname):
    if not os.path.exists(f"./static/images/documentation/{dirname}"):
        os.mkdir(f"./static/images/documentation/{dirname}")
    else:
        pass

def newLog(request):
    if (request.method == "POST"):
        new = Log.objects.create(
            dateLog=datetime.datetime.strptime(request.POST['Date'], '%Y-%m-%d').date(),
            logDiary=request.POST['Log']
        )

        for file in request.FILES.getlist('file'):
            dir_documentation(request.POST['Date'])
            handle_uploaded_file(f=file, dir=request.POST['Date'])
            newImg = imgDoc.objects.create(
                dirname=request.POST['Date'],
                filename=str(file)
            )
            new.filesDocumentation.add(newImg)
    return redirect('/')

def editLog(request):
    edit = Log.objects.get(id=request.POST['edit-log-id'])
    edit.dateLog = datetime.datetime.strptime(request.POST['tanggal-edit'], '%Y-%m-%d').date()
    edit.logDiary = request.POST['log-edit']
    for file in request.FILES.getlist('file-edit'):
        dir_documentation(request.POST['tanggal-edit'])
        handle_uploaded_file(f=file, dir=request.POST['tanggal-edit'])
        newImg = imgDoc.objects.create(
            dirname=request.POST['tanggal-edit'],
            filename=str(file)
        )
        edit.filesDocumentation.add(newImg)
    edit.save()
    return redirect('/')

def deleteLogBook(request):
    log = Log.objects.get(id=request.POST['delete-id'])
    log.delete()
    return redirect('/')

# Create your views here.
def indexViews(request):
    print(request.user)
    if (str(request.user) == 'AnonymousUser'):
        return redirect('/splash')

    dataLog = Log.objects.all().order_by('-id')
    contexts = {
        'logData': dataLog
    }
    return render(request, 'index.html', context=contexts)

def loginViews(request):
    if (str(request.user) != 'AnonymousUser' and request is not None):
        return redirect('/')
    form = RegisterForm()
    return render(request, 'login.html', context={"form": form})

def logoutViews(request):
    if request.method == 'POST':
        logout(request)
    return redirect('/auth')

def logincekViews(request):
    if request.method == 'POST':
        username = request.POST['usernameform']
        password = request.POST['passwordform']
        user = authenticate(username=username, password=password)
        if (user is not None):
            login(request, user)
        else:
            form = RegisterForm()
            return render(request, 'login.html', {"form": form, "loginfalse": True})
    else:
        return redirect('/')
    return redirect('/')

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            user = form.save()
            login(response, user)
            return redirect("/")
        else:
            form = RegisterForm()
    else:
        form = RegisterForm()
        return render(response, 'login.html', context={"form": form})

    return render(response, "index.html")

def splashviews(request):
    return render(request, 'splashscreen.html')