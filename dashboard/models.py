from django.db import models

# Create your models here.

class Grade(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()

    def __str__(self):
        # return str(self.name +' '+ str(self.year))
        return str(self.name)

class Student(models.Model):
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    regid = models.CharField(max_length=200)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.first +' '+ str(self.last))
    
class Staff(models.Model):
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    empid = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=200,null=True,blank=True)

    def __str__(self):
        return str(self.first +' '+ str(self.last))
        
