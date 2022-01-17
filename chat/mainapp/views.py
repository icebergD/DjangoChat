from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView, View, CreateView

from django.contrib.auth import authenticate, login
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import logout

# from .models import Notebook, Smartphone 




# Create your views here
def hello(request):
	return HttpResponse("Hello world")

#@login_required(login_url='login/')
def BaseView(request):
	authed = request.user.is_authenticated
	context = {
		'authed': authed,		
	}
	return render(request,'base.html',context)


def user_login(request):
	authed = request.user.is_authenticated
	context = {
		'authed': authed
	}
	if request.method == 'POST':
		form = UserLoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(username=cd['username'], password=cd['password'])
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect(reverse('base'))
				else:
					return HttpResponse('Disabled account')
			else:
				form = UserLoginForm()
				context['form'] = form
				return render(request, 'login.html', context)
	else:
		form = UserLoginForm()
		context['form'] = form
	return render(request, 'login.html', context)

def user_register(request):
	authed = request.user.is_authenticated
	context = {
		'authed': authed,		
	}
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)

		if form.is_valid():
			cd = form.cleaned_data
			user = User.objects.create_user(username=cd['username'], first_name=cd['first_name'], email=cd['email'], password=cd['password'])
			user.save()
            
			return HttpResponseRedirect('/login/')
            # user = authenticate(username=cd['username'], password=cd['password'])
            # if user is not None:
            #     if user.is_active:
            #         login(request, user)
            #         return HttpResponse('Register successfully')
            #     else:
            #         return HttpResponse('Disabled account')
            # else:
            #     return HttpResponse('Invalid register')
	else:
		form = UserRegistrationForm()
		context['form'] = form
	return render(request, 'register.html', context)
   
def user_logout(request):
	logout(request)
	authed = request.user.is_authenticated
	context = {
		'authed': authed,		
	}
	return render(request,'logged_out.html',context)

# class RegisterUser(CreateView):

# 	form_class = UserCreationForm
# 	template_name = 'register.html'
# 	success_url = reverse_lazy('login')

# 	def get_context_data(self, *, object_list=None, **kwargs):
# 		context = super().get_context_data(**kwargs)
# 		c_def = self.get_user_context(title="Регистрация")
# 		return dict(list(context.items()) + list(c_def.items()))