from django.db import models

# Create your models here.
class user(models,Models):
user_name=models.CharField(max_length=50)
mobile_no=models.IntegerField(max_length=10)
acc_no=models.IntegerField(max_length=15)
email_id=models.CharField(max_length=20)
atm_pin=models.IntegerField(max_length=4)

def _str_(self):
 return self.name

class Deposit(models,Models):
account=models ForeignKey(user,on_delete=models.CASCADE)
deposit_money=models.IntergerField(max_length=10)

def _str_(self):
 retrun self.name

class withdraw(models,Models):
account=models ForeignKey(user,on_delete=models.CASCADE)
withdraw_money=models.IntergerField(max_length=10)

def _str_(self):
 return self.name


