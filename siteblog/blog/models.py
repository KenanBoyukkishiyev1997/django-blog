from django.db import models
from django.urls import reverse

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='url',unique=True)


    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return reverse('category',kwargs={"slug": self.slug})

    class Meta:
        ordering=['title']


    



class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, verbose_name='url',unique=True)


    def get_absolute_url(self):
        return reverse('tag',kwargs={"slug": self.slug})



    def __str__(self):
        return self.title




    class Meta:
        ordering=['title']




class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='url',unique=True)
    author = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, )
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/',blank='true')
    views =  models.IntegerField(default=0)
    category= models.ForeignKey(Category,on_delete=models.PROTECT, related_name='posts')
    tag=models.ManyToManyField(Tag,blank=True,related_name='posts')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post',kwargs={"slug": self.slug})

    
    class Meta:
        ordering=['-created_at']

    



# Create your models here.
