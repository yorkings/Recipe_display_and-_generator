# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Category(models.Model):
  name=models.CharField(max_length=100)
  def __str__(self):
    return self.name

class Post(models.Model):
  author=models.ForeignKey(User,on_delete=models.CASCADE)
  categories = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="posts")
  image=models.ImageField(upload_to='posts',default='food.webp')
  title=models.CharField(max_length=250)
  slug=models.SlugField()
  ingredients= RichTextField(null=True,blank=True)
  body= RichTextField(null=True,blank=True)
  publish = models.DateTimeField(default=timezone.now)
  created = models.DateTimeField(auto_now_add=True)
  class Meta:
    ordering=['title']
  def __str__(self):
    return self.title
  


class Profile(models.Model):
  user=models.OneToOneField(User, on_delete=models.CASCADE )
  bios= models.CharField(max_length=250 ,blank=True,null=True)
  image=models.ImageField(default='default_prof.png',upload_to='profile_pic')
  mobile_no = PhoneNumberField(blank=True)
  location=models.CharField(max_length=250,null=True,blank=True)
  def __str__(self):
      return f'{self.user.username} Profile'

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    def __str__(self):
     return self.post


class Cosmetics(models.Model):
   author=models.CharField(max_length=100)
   title=models.CharField(max_length=50)
   content= RichTextField(null=True,blank=True)
   def __str__(self):
    return f'{self.author}  : {self.title}'



class Learning(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='learning/images', blank=True, null=True)
    video = models.FileField(upload_to='learning/videos', blank=True, null=True)
    ingredients = RichTextField(null=True, blank=True)
    procedure = RichTextField(null=True, blank=True)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='medium')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user.username} Learning'

   
