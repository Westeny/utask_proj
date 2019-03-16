from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from app.models import Task, Vidicap
from django.contrib.auth.decorators import login_required
from django.utils.dateparse import parse_date



def index(request):
    if request.user.is_authenticated:
        return dashboard(request)

    else:
        return render_to_response('login.html')

def timeline(request):
    return render_to_response('timeliner.html')


def vidicap_info(request):
    context = {'vidicap': Vidicap.objects.all()}
    return render_to_response('vidicap.html', context)

def add_new_vidicap(request):
    new_vidicap = Vidicap(vidicap_model = request.POST['vidicap_model'],
                          sell_date = parse_date(request.POST['sell_date']),
                          set_up_place = request.POST['set_up_place'],
                          note = request.POST['note'])
    new_vidicap.save()
    response= {'message': 'Запись добавлена'}
    return JsonResponse(response)



@login_required
def dashboard(request):
    context = {'tasks': Task.objects.filter(user=request.user), 'user': User.objects.all()}
    return render_to_response('index.html', context)


def add_new_task(request):
    user = request.POST['user']
    n_task = Task(user = User.objects.get(username=user),
                  task_name = request.POST['task'],
                  deadline_date = parse_date(request.POST['deadline_date']),
                  tags = request.POST['tag'],
                  note = request.POST['note'])
    n_task.save()
    response= {'message': 'Запись добавлена'}
    return JsonResponse(response)





""" login and registration"""

def singin_user(request):
    user = authenticate(
        username = request.POST['username'],
        password = request.POST['password'])
    if user is None:
        return render_to_response('error.html')
    else:
        login(request, user)
        return HttpResponseRedirect('/')


def reg(request):
    return render_to_response('registration.html')


def new_user_reg(request):
    user = User.objects.create_user(
        email=request.POST['email'],
        username=request.POST['username'],
        password=request.POST['password'])
    login(request, user)
    return HttpResponseRedirect('/')



def do_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

