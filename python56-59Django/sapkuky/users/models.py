from django.db import models

# Create your models here.
class Person(models.Model):
    person_firstname=models.CharField(max_length=100)
    person_lastname=models.CharField(max_length=100)
    person_phone=models.CharField(max_length=10)
    person_email=models.CharField(max_length=100)
    def __str__(self):
        return f'{self.id}'

class User(models.Model):
    user_nickname=models.CharField(max_length=100)
    user_password=models.CharField(max_length=255)
    user_active=models.BooleanField()
    person_id=models.ForeignKey(Person,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return f'User#:{self.id}:{self.user_nickname}:{self.user_password}:{self.user_active}'
        
 

