from django.db import models

# Create your models here.
class hospital(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    gender=models.CharField(max_length=20)
    mobile_no=models.IntegerField()
    
    def __str__(self):
        return self.name


class client(models.Model):
    patient_code=models.IntegerField()
    patient_name=models.CharField(max_length=20)
    age=models.IntegerField()
    dob=models.IntegerField()
    gender=models.CharField(max_length=20)
    father_name=models.CharField(max_length=20)
    husband_name=models.CharField(max_length=20)
    disease=models.CharField(max_length=20)
    blood_group=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    mobile_no=models.IntegerField()
    email=models.EmailField(max_length=20)
    patient_name=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    blood_group=models.CharField(max_length=20)


    def __str__(self):
        return self.patient_name

