from django.db import models
from django.utils import timezone

# Create your models here.
class Admin(models.Model):
    username=models.CharField(max_length=150)
    password=models.CharField(max_length=150)
    
    def __str__(self):
        return self.username

class Category(models.Model):
    name=models.CharField(max_length=150)
    issue_date=models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name 
    
    
class User(models.Model):
    name = models.CharField(max_length=150)
    password = models.CharField(max_length=150)    
    email = models.EmailField()
    mobile = models.BigIntegerField()
    image = models.ImageField(upload_to='profile_image/',default='img')
    

    
    def __str__(self):
        return self.name
    
class Policy(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    policy_name=models.CharField(max_length=150)
    policy_desc=models.TextField()
    sum_insurance=models.BigIntegerField()
    premium=models.BigIntegerField()    
    tenure=models.BigIntegerField()
    creation_date=models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.policy_name
    
class PolicyRecord(models.Model):
    customer= models.ForeignKey(User, on_delete=models.CASCADE)
    policy= models.ForeignKey(Policy, on_delete=models.CASCADE)
    status = models.CharField(max_length=100,default='Pending')
    creation_date =models.DateField(auto_now=True)
    def __str__(self):
        return self.policy
    
class Policyapply(models.Model):
    customer= models.ForeignKey(User, on_delete=models.CASCADE)
    policy= models.ForeignKey(Policy, on_delete=models.CASCADE)
    status = models.CharField(max_length=100,default='Pending')
    creation_date =models.DateField(auto_now=True)
    def __str__(self):
        return self.customer.name

class Question(models.Model):
    customer= models.ForeignKey(User, on_delete=models.CASCADE)
    description =models.CharField(max_length=500)
    admin_comment=models.CharField(max_length=200,default='Nothing')
    asked_date =models.DateField(auto_now=True)
    def __str__(self):
        return self.customer.name