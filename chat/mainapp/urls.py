from django.urls import path, include
from .views import (
	hello, 
	BaseView,
	user_login,
	user_register,
	user_logout,
	send_message,
	update_message
)

urlpatterns = [
	path('', BaseView, name='base'),
	path('login/', user_login, name='login'),
	path('register/', user_register, name='register'),
	path('logout/', user_logout, name='logout'),
	path('send-message/', send_message, name='send_message'),
	path('update-message/', update_message, name='update_message'),


    
]
