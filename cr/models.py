from django.db import models
from django.contrib import admin

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    name = models.CharField(max_length=50)
    num = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    
    
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email','name','num','major')

class zhengxin(models.Model):
	roomID = models.CharField(max_length=10);
	Monday = models.CharField(max_length=10);
	Tuesday = models.CharField(max_length=10);
	Wednesday = models.CharField(max_length=10);
	Thursday = models.CharField(max_length=10);
	Friday = models.CharField(max_length=10);
	Saturday = models.CharField(max_length=10);
	Sunday = models.CharField(max_length=10);
	num = models.IntegerField();
    
class zhizhi(models.Model):
	roomID = models.CharField(max_length=10);
	Monday = models.CharField(max_length=10);
	Tuesday = models.CharField(max_length=10);
	Wednesday = models.CharField(max_length=10);
	Thursday = models.CharField(max_length=10);
	Friday = models.CharField(max_length=10);
	Saturday = models.CharField(max_length=10);
	Sunday = models.CharField(max_length=10);
	num = models.IntegerField();

class chengyi(models.Model):
	roomID = models.CharField(max_length=10);
	Monday = models.CharField(max_length=10);
	Tuesday = models.CharField(max_length=10);
	Wednesday = models.CharField(max_length=10);
	Thursday = models.CharField(max_length=10);
	Friday = models.CharField(max_length=10);
	Saturday = models.CharField(max_length=10);
	Sunday = models.CharField(max_length=10);
	num = models.IntegerField();


class zhulou(models.Model):
	roomID = models.CharField(max_length=10);
	Monday = models.CharField(max_length=10);
	Tuesday = models.CharField(max_length=10);
	Wednesday = models.CharField(max_length=10);
	Thursday = models.CharField(max_length=10);
	Friday = models.CharField(max_length=10);
	Saturday = models.CharField(max_length=10);
	Sunday = models.CharField(max_length=10);
	num = models.IntegerField();
        
admin.site.register(User,UserAdmin)