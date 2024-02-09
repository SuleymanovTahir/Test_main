from django.urls import path
from . import views


urlpatterns=[
    path('',views.index,name='home'),
    path('icecream/<str:adress>',views.icecream_detail,name='icecream_detail')
]