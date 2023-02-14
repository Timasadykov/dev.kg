from django.db import models

from apps.company.models import Company


class Event(models.Model):
    date = models.DateTimeField(verbose_name='Дата и время  провождения')
    name = models.CharField(max_length=127,verbose_name='назвние ')
    location = models.CharField(max_length=127,verbose_name='локации')
    image = models.ImageField(upload_to='event/images/',verbose_name='картинки')
    description = models.TextField(verbose_name='описание')
    company = models.ForeignKey(Company, on_delete=models.CASCADE,related_name='events', verbose_name='Компания')

    def __str__(self) :
        return self.name
    
    class Meta:
        verbose_name = 'мкроприятие'
        verbose_name_plural = 'мероприятия'
