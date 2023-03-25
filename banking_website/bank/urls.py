from django.contrib import admin
from django.urls import path
from . import views
from .views import get_branches
urlpatterns = [

    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('btn/',views.btn,name='btn'),
    path('register/',views.register,name='register'),
    path('form/',views.form,name='form'),
    path('get_branches/<int:district_id>/',views.get_branches,name='get_branches'),
    # path('get_branches/<int:district_id>/', views.get_branches, name='get_branches'),
    # path('msg/',views.msg,name='msg'),

    path('logout/',views.logout,name='logout'),
    # path('load_states/',views.load_states,name='load_states')

]
