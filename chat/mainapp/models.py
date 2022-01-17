from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Message(models.Model):
	owner = models.ForeignKey(User, null=True, verbose_name='Владелец', on_delete=models.CASCADE)
	message = models.TextField(verbose_name='Сообщение', null=True, blank=True)
	created_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания заказа')

	def __str__(self):
		return 'Имя Пользователя: {} Дата создания сообщения: {}'.format(self.owner, self.created_at)
