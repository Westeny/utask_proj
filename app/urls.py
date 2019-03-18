from django.urls import path
from app.views import *

urlpatterns = [
    path('', index),
    path('login', singin_user),
    path('registration', reg),
    path('new_user_add', new_user_reg),
    path('logout', do_logout),
    path('add_new_task', add_new_task),
    path('task_get_info_for_change', task_get_info_for_change),
    path('task_change', task_change),
    path('task_delete', task_delete),
    path('task_complite',task_complite),
    path('timeliner', timeline),
    path('vidicaps', vidicap_info),
    path('add_new_vidicap', add_new_vidicap),
    path('vidicap_complite', vidicap_complite),
    path('vidicap_get_info_for_change', vidicap_get_info_for_change),
    path('vidicap_change', vidicap_change),
    path('tenders', tenders_info),
    path('add_new_tender', add_new_tender),
    path('tender_delete',tender_delete),
    path('tender_get_info_for_change',tender_get_info_for_change),
    path('tender_change',tender_change)
]

