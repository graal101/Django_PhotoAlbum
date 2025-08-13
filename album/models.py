from django.db import models
from django.utils import timezone

# Create your models here.
class Visitors(models.Model):
    ip = models.CharField('IP', max_length=20, null=True, blank=True)  # IP-адрес
    user_agent = models.TextField('User_Agent', max_length=200, null=True, blank=True)  # User-Agent
    visittime = models.DateTimeField('Date_Time', default=timezone.now)  # Время визита
    
    class Meta:
        verbose_name = 'Визитер'  # Единственное название
        verbose_name_plural = 'Визитеры'  # Множественное название
    
    # Для корректного отбражения в БД
    def __str__(self):
        return f"Посещение с {self.ip}  в {self.visittime}"
        
