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
  
  
  
