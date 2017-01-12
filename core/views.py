from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader
from django.contrib.auth.decorators import login_required
from core.models import *

# Create your views here.
def index(request):
	return render(request, 'index.html')

def order(request):
	menu_item = MenuItem.objects.all()
	context = {
		'menu_item': menu_item
	}
	return render(request, 'order.html', context)

