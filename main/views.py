from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from record.models import Record
from client.models import Client
from live.models import Live

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request,username=username, password=password)

        if user != None:
            auth.login(request, user)
            return redirect('home')
        else:
            print('error')
    return render(request, 'login.html')


@login_required
def home(request):
    return render(request, 'index.html')

@login_required
def clients(request):
    clients = Client.objects.all().order_by('-id')
    context = {
        'clients': clients,
    }
    return render(request, 'users.html', context)

@login_required
def live(request):
    lives = Live.objects.filter(is_live=True).order_by('-id')
    context = {
        'lives': lives,
    }
    return render(request, 'live.html' , context)

@login_required
def recorded(request):
    records = Record.objects.all().order_by('-id')
    context = {
        'records': records,
    }
    return render(request, 'record.html' , context)

def start_live(request, ip):
    try:
        client = Client.objects.get(devive_IP=ip)
        if client != None:
            live = Live.objects.create(client=client, is_live=True)
            live.save()
    except:
        pass

def stop_live(request, ip):
    try:
        client = Client.objects.get(devive_IP=ip)
        if client != None:
            live = Live.objects.filter(client=client, is_live=True)
            live.is_live = False
            live.save()
    except:
        pass