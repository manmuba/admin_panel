from django.forms import model_to_dict
from django.http import Http404, JsonResponse
from django.core import serializers
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
    clients = Client.objects.all().count()
    records = Record.objects.all().order_by('-id').count()
    lives = Live.objects.filter(is_live=True).order_by('-id').count()
    context = {
        'lives': lives,
        'clients': clients,
        'records': records,
    }
    return render(request, 'index.html', context)

@login_required
def clients(request):
    clients = Client.objects.all()
    context = {
        'clients': clients,
    }
    return render(request, 'users.html', context)

@login_required
def add_clients(request):
    if request.method == 'POST':
        first_name      = request.POST['first_name']
        last_name       = request.POST['last_name']
        email           = request.POST['email']
        phone           = request.POST['phone']
        ip              = request.POST['ip']
        client = Client.objects.create(
            first_name  = first_name,
            last_name   = last_name,
            email       = email,
            phone       = phone,
            device_IP   = ip
        )
        client.save()
        return redirect('clients')
    return render(request, 'create_user.html')

@login_required
def delete_client(request, email):
    try:
        client = Client.objects.get(email=email)
        client.delete()
        return redirect('clients')
    except Client.DoesNotExist:
        raise Http404("Client does not exist")

@login_required
def live(request):
    return render(request, 'live.html')

@login_required
def recorded(request):
    records = Record.objects.all().order_by('-id')
    context = {
        'records': records,
    }
    return render(request, 'record.html' , context)

@login_required
def get_live_data(request):
    data = []
    for live in Live.objects.all():
        live_dict = model_to_dict(live)
        live_dict['client'] = model_to_dict(live.client)
        data.append(live_dict)
    return JsonResponse({'data': data})

def start_live(request, ip):
    try:
        client = Client.objects.get(device_IP=ip)
        if client != None:
            live = Live.objects.create(client=client, is_live=True)
            live.save()
    except:
        pass

def stop_live(request, ip):
    try:
        client = Client.objects.get(device_IP=ip)
        if client != None:
            live = Live.objects.filter(client=client, is_live=True)
            for i in live:
                i.delete()
    except:
        pass