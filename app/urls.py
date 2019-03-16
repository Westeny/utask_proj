from django.urls import path
from app.views import *

urlpatterns = [
    path('', index),
    path('login', singin_user),
    path('registration', reg),
    path('new_user_add', new_user_reg),
    path('logout', do_logout),
    path('add_new_task', add_new_task),
    path('timeliner', timeline),
    path('vidicaps', vidicap_info)
]

