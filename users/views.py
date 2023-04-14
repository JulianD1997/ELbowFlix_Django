from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import UserForm

# Create your views here.

def register(request):
    form = UserForm()
    context={'form':form}
    return render(request,'users/register.html',context)