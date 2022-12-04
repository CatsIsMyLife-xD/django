from django.db import models

class Task(models.Model):
    tittle  =   models.CharField('Название',  max_length=50)
    task    =   models.TextField('Описание')

    def __str__(self):
        return  self.tittle
        
    class Meta:
        verbose_name    =   'Задача'
        verbose_name_plural =   'Задачи'
        
class Organization(models.Model):
    tittle  =   models.CharField('Краткое название',  max_length=50)
    name  = models.TextField('Название')
    address  = models.TextField('Адрес')
    phone = models.TextField('Телефон')
    
    def __str__(self):
        return  self.tittle
    
    class Meta:
        verbose_name    =   'Организация'
        verbose_name_plural =   'Информация'

class Catalog(models.Model):
    code = models.IntegerField('Код')
    product_name  =   models.CharField('Краткое название',  max_length=50)
    image = models.ImageField('Изображение' ,upload_to='images/')
    price = models.FloatField('Цена')
    description = models.TextField('Описание товара')
    
    def __str__(self):
        return  self.product_name
    
    class Meta:
        verbose_name    =   'Товар'
        verbose_name_plural =   'Информация о товарах'

class News(models.Model):
    news_name  =  models.CharField('Краткое описание',  max_length=50)
    news_image = models.ImageField('Изображение' ,upload_to='images/')
    news_description = models.TextField('Описание новости')
    
    def __str__(self):
        return  self.news_name
    
    class Meta:
        verbose_name    =   'Новость'
        verbose_name_plural =   'Информация о новости'   
    
# Create your models here.
