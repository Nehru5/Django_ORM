from django.db import models

class Mobile(models.Model):
  name = models.CharField(max_length=200)
  price = models.DecimalField(decimal_places=2,max_digits=10)
  ram = models.PositiveIntegerField()
  rom = models.PositiveIntegerField()
  battery = models.PositiveIntegerField()
  processor = models.CharField(max_length=200)
  camera = models.PositiveIntegerField()
  supplier = models.CharField(max_length=100)
  
  def __str__(self):
    return self.name
  
  

class User(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField()
  
  def __str__(self):
    return self.name
  
  
class UserProfile(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  bio = models.TextField()
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=100)
  phone = models.CharField(max_length=20)
  
  def __str__(self):
    return f"{self.user.name}'s Profile"
  
  

class Category(models.Model):
  name = models.CharField(max_length=100)
  
  def __str__(self):
    return self.name
  
  
class Product(models.Model):
  category = models.ForeignKey(Category,on_delete=models.CASCADE)
  name = models.CharField(max_length=200)
  price = models.DecimalField(max_digits=10,decimal_places=2)
  supplier = models.CharField(max_length=100)
  
  def __str__(self):
    return self.name
  
  
  
class Course(models.Model):
  name = models.CharField(max_length=200)
  
  def __str__(self):
    return self.name
  
  
class Student(models.Model):
  course = models.ManyToManyField(Course)
  name = models.CharField(max_length=200)
  department = models.CharField(max_length=100)
  
  def __str__(self):
    return self.name
