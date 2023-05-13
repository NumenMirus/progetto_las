from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('insert_into_db/', views.insert_into_db, name='insert_into_db'),
    # path('login/', views.login, name='login'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('testload/', views.test_load, name='testload'),
    path('get_events/', views.get_events, name='get_events'),
]