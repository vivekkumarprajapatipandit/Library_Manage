from django.db import models


class Bookdata(models.Model):
    id = models.IntegerField(primary_key=True)
    BookName = models.CharField(max_length=50)
    Description  = models.CharField(max_length=500)
    Author = models.CharField(max_length=50)
    Price = models.IntegerField()
    Category = models.CharField(max_length=50)
    Pages = models.IntegerField()
    Date_Of_Publish = models.DateField()
    Photo = models.ImageField(upload_to='profile_pics',blank=True)
    
class Details(models.Model):
    id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=100)
    Username  = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Password = models.CharField(max_length=20)
    DOB = models.DateField()
    Gender = models.CharField(max_length=10)
    Language = models.CharField(max_length=50)
    Aadhar = models.IntegerField()
    Profilepic = models.ImageField(upload_to='profile_pics',blank=True)  
 

 