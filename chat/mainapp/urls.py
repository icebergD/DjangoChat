from django.urls import path, include
from .views import (
	hello, 
	BaseView,
	user_login,
	user_register,
	user_logout
)

urlpatterns = [
	path('', BaseView, name='base'),
	path('login/', user_login, name='login'),
	path('register/', user_register, name='register'),
	path('logout/', user_logout, name='logout'),
	# path('login/', include('django.contrib.auth.views.login'), name='login'),
	# path('logout/', include('django.contrib.auth.views.logout'), name='logout'),
	# path('logout-then-login/', include('django.contrib.auth.views.logout_then_login'), name='logout_then_login'),
    
]
