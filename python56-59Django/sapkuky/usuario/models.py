from django.db import models

# Create your models here.
class Roll(models.Model):
    name=models.CharField(max_length=60)
    roll_description=models.CharField(max_length=120)
    def __str__(self):
        return self.name
    
class Usuario(models.Model):
    name=models.CharField(max_length=60)
    firstname=models.CharField(max_length=60)
    age=models.IntegerField()
    status=models.BooleanField()
    roll_id=models.ForeignKey(Roll,on_delete=models.SET_NULL,null=True)
    


    