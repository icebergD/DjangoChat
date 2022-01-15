from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView, View

# from .models import Notebook, Smartphone 
# from .forms import OrderForm



# Create your views here
def hello(request):
	return HttpResponse("Hello world")

class BaseView(View):
	def get(self, request, *args, **kwargs):
	
		info = 'Hello'
		context = {
			'info': info,
			
		}
		return render(request,'base.html',context)

