from django.shortcuts import render,get_object_or_404
from .models import *




def index(request):
    profiles=Profile.objects.order_by('pk')
    context={
        'title':'text',
        'profiles':profiles
    }
    return render(request,'mains/index.html',context=context)

