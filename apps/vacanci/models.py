from django.db import models

from apps.company.models import Company


class Vacanci(models.Model):
    name = models.CharField(max_length=127,verbose_name='назвние ')
    сompany = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacances', verbose_name='Компания')
    post = models.CharField(max_length=127,verbose_name='Должность')
    selery = models.CharField(max_length=127, verbose_name='Оклад')
    type_work = models.CharField(max_length=127,verbose_name='тип')
    description = models.TextField(verbose_name='описание')
    email= models.EmailField('почта')
    
    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'