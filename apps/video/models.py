from django.db import models

from apps.company.models import Company


class Video(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='videos', verbose_name='Компания')
    date = models.DateField(verbose_name='Дата выхода видео')
    name = models.CharField(max_length=127,verbose_name='назвние ')
    video = models.FileField(upload_to='video/videos/')
    description = models.TextField('Описание')

    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name = 'видео'
        verbose_name_plural = 'видео'