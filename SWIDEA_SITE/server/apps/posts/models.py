from django.db import models

# Create your models here.
class IdeaStar(models.Model):
    set = models.BooleanField(default=False)

class Dev(models.Model):
    name = models.CharField(max_length=12)
    kind = models.CharField(max_length=12)
    content = models.TextField()

class Post(models.Model):
    title = models.CharField(max_length=12)
    photo = models.ImageField(blank=True, upload_to='posts/%Y%m%d')
    content = models.TextField()
    interest = models.PositiveIntegerField(default = 0)
    devtool = models.ForeignKey(Dev, on_delete=models.CASCADE) #하나의 dev는 여러개의 post로 이루어짐
    star = models.OneToOneField(IdeaStar, null=True, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
