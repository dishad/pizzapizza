from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
	return render(request, 'index.html')

