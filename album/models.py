from django.db import models
from django.utils import timezone


class Visitors(models.Model):
    ip = models.CharField('IP', max_length=20, null=True, blank=True)  # IP-адрес
    user_agent = models.TextField('User_Agent', max_length=200, null=True, blank=True)  # User-Agent
    ref = models.TextField('Referer', max_length=200, null=True, blank=True)  # Referer
    visittime = models.DateTimeField('Date_Time', default=timezone.now)  # Время визита
    
    class Meta:
        verbose_name = 'Визитер'  # Единственное название
        verbose_name_plural = 'Визитеры'  # Множественное название
    
    # Для корректного отбражения в БД
    def __str__(self):
        return f"Посещение с {self.ip}  в {self.visittime}"
        
        
class UplPict(models.Model):
    """Store photo in file system with path in db."""
    name = models.CharField(max_length=150)
    UpPict_Img = models.ImageField(upload_to='images/')
    
    class Meta:
        verbose_name = 'Загрузка'  # Единственное название
        verbose_name_plural = 'Загрузки'  # Множественное название
    
    def __str__(self):
        return f"Загружено: {self.name}"
        
        
