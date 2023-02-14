from django.db import models


class Company(models.Model):
    logo = models.ImageField(upload_to='company/logos/',verbose_name='логотип компании')
    name = models.CharField(max_length=127, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    telegram = models.URLField(verbose_name='телеграм')
    whatsapp = models.URLField(verbose_name='вотс апп')

    @property
    def vacanci_amount(self):
        return self.vacances.count()
    
    @property
    def event_amount(self):
        return self.events.count()
    
    @property
    def video_amount(self):
        return self.videos.count()
    
    
    
    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name = 'компания'
        verbose_name_plural = 'компании'
