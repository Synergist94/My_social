from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField('Название новости', max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True,verbose_name='Адрес новости на англиском')
    text = models.TextField('Краткое описание новости')
    full_text = models.TextField('Полное описание новости',blank=True)
    author = models.ForeignKey(User, on_delete= models.PROTECT, related_name='post_user')
    category = models.ForeignKey('Category', on_delete= models.PROTECT,verbose_name='Категория',related_name='post_category')
    created_on = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        
    def get_absolute_url(self):
        return reverse('blog', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
    
class Category(models.Model):
    title = models.CharField('Название категории', max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})

    def __str__(self):
        return self.title