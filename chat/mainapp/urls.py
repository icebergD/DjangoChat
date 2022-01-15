from django.urls import path
from .views import (
	hello, 
	BaseView, 
)

urlpatterns = [
	path('', BaseView.as_view(), name='base'),
    
]
