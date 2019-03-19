from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from app.models import Task, Vidicap, Tenders
from django.contrib.auth.decorators import login_required
from django.utils.dateparse import parse_date



def index(request):
    if request.user.is_authenticated:
        return dashboard(request)

    else:
        return render_to_response('login.html')


"""task managment part"""

@login_required
def dashboard(request):
    context = {'tasks': Task.objects.filter(user=request.user).order_by('is_complete').order_by('deadline_date'), 'user': User.objects.all()}
    return render_to_response('index.html', context)

@login_required
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


@login_required
def task_get_info_for_change(request):
    task_to_cahnge = Task.objects.get(id=request.POST['id_to_change'])
    response = {'idchange':request.POST['id_to_change'],
                'task_name_to_change': task_to_cahnge.task_name,
                'deadline_date_to_change': task_to_cahnge.deadline_date,
                'tag_to_change': task_to_cahnge.tags,
                'note_to_change': task_to_cahnge.note}
    return JsonResponse(response)


@login_required
def task_change(request):
    user = request.POST['user']
    n_task = Task(user=User.objects.get(username=user),
                  task_name=request.POST['task'],
                  deadline_date=parse_date(request.POST['deadline_date']),
                  tags=request.POST['tag'],
                  note=request.POST['note'])
    n_task.save()
    task = Task.objects.get(id=request.POST['id'])
    task.delete()
    response = {'message':'запись изменена'}
    return JsonResponse(response)


@login_required
def task_complite(request):
    task = Task.objects.get(id=request.POST['id_to_complite'])
    task.complite()
    task.save()
    response = {'message':'Задача завершена'}
    return JsonResponse(response)


@login_required
def task_delete(request):
    task = Task.objects.get(id=request.POST['id_to_delete'])
    task.delete()
    response = {'message': 'запись удалена'}
    return JsonResponse(response)


"""vidicap info part"""
@login_required
def vidicap_info(request):
    context = {'vidicap': Vidicap.objects.all().order_by('-sell_date')}
    return render_to_response('vidicap.html', context)


@login_required
def add_new_vidicap(request):
    add_vidicap(request)
    response= {'message': 'Запись добавлена'}
    return JsonResponse(response)


def add_vidicap(request):
    new_vidicap = Vidicap(vidicap_model = request.POST['vidicap_model'],
                          sell_date = parse_date(request.POST['sell_date']),
                          set_up_place = request.POST['set_up_place'],
                          note = request.POST['note'])
    new_vidicap.save()
    return


@login_required
def vidicap_complite(request):
    vidicap = Vidicap.objects.get(id=request.POST['id_to_complite'])
    vidicap.complite()
    vidicap.save()
    response = {'message':'Done'}
    return JsonResponse(response)


@login_required
def vidicap_get_info_for_change(request):
    vidicap_to_cahnge = Vidicap.objects.get(id=request.POST['id_to_change'])
    response = {'idchange':request.POST['id_to_change'],
                'vidicap_model_change': vidicap_to_cahnge.vidicap_model,
                'sell_data_change': vidicap_to_cahnge.sell_date,
                'set_up_place_change': vidicap_to_cahnge.set_up_place,
                'note_change': vidicap_to_cahnge.note}
    return JsonResponse(response)


@login_required
def vidicap_change(request):
    add_vidicap(request)
    vidicap_del = Vidicap.objects.get(id=request.POST['id'])
    vidicap_del.delete()
    response = {'message': 'запись изменена'}
    return JsonResponse(response)


"""timeline part"""
@login_required
def timeline(request):
    not_complite_task = Task.objects.filter(user=request.user).order_by('-deadline_date')
    complite_task = Task.objects.filter(is_complete=True)
    context = {'not_complite_task': not_complite_task,
               'complite_task': complite_task}
    return render_to_response('timeliner.html', context)





"""tenders_info part"""

def add_tender(request):
    n_tender = Tenders(tender_number=request.POST['tender_number'],
                       tender_lot=request.POST['tender_lot'],
                       budget=request.POST['budget'],
                       date_podacha=parse_date(request.POST['date_podacha']),
                       date_tender=parse_date(request.POST['date_tender']),
                       buyer=request.POST['buyer'],
                       customer=request.POST['customer'],
                       sum_offer=request.POST['sum_offer'],
                       note=request.POST['note'])
    n_tender.save()
    return


@login_required
def tenders_info(request):
    context = {'tenders': Tenders.objects.all()}
    return render_to_response('tenders.html', context)


@login_required
def add_new_tender(request):
    add_tender(request)
    response= {'message': 'Запись добавлена'}
    return JsonResponse(response)


@login_required
def tender_delete(request):
    print(request.POST)
    tender = Tenders.objects.get(id=request.POST['id_to_delete'])
    tender.delete()
    response = {'message': 'запись удалена'}
    return JsonResponse(response)


@login_required
def tender_get_info_for_change(request):
    tender_to_cahnge = Tenders.objects.get(id=request.POST['id_to_change'])
    response = {'id_to_change':request.POST['id_to_change'],
                'tender_number':tender_to_cahnge.tender_number,
                'tender_lot':tender_to_cahnge.tender_lot,
                'budget':tender_to_cahnge.budget,
                'date_podacha':tender_to_cahnge.date_podacha,
                'date_tender':tender_to_cahnge.date_tender,
                'buyer':tender_to_cahnge.buyer,
                'customer':tender_to_cahnge.customer,
                'sum_offer':tender_to_cahnge.sum_offer,
                'note':tender_to_cahnge.note}
    return JsonResponse(response)


@login_required
def tender_change(request):
    add_tender(request)
    tender_del = Tenders.objects.get(id=request.POST['id'])
    tender_del.delete()
    response = {'message':'запись изменена'}
    return JsonResponse(response)


""" login and registration"""

def singin_user(request):
    print(request.POST)
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
    print(request.POST)
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

