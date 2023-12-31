from django.db import models

# Create your models here.

class Dept(models.Model):
    name = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Role(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name



class Emp(models.Model):
    fname = models.CharField(max_length=100, null=False)
    lname = models.CharField(max_length=100)
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)        
    bonus = models.IntegerField(default=0) 
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phoneNo = models.IntegerField(default=0)        
    joinDate = models.DateField()      

    def __str__(self):
        return "%s %s" %(self.fname, self.lname)