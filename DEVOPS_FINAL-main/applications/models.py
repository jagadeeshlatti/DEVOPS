from django.db import models
from django.core.exceptions import ValidationError
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    username = None
    first_name = None
    last_name = None
    
    email = models.EmailField(primary_key=True)
    name = models.CharField(max_length=255)
    is_email_verified = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    objects = CustomUserManager()

    def __str__(self):
        return self.name
    
class registerecandidates(models.Model):
    id = models.BigAutoField(primary_key=True)
    candidateName=models.CharField(max_length=30)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=20)
    datecreated=models.DateTimeField(auto_now_add=True,null=True)


def __str__(self):
        return self.candidateName

def  validate_contactno(value):
      if(len(value)==10):
           return value
      else:
           raise ValidationError("Enter valid mobile number")

def  validate_Adhaarno(value):
      if(len(value)==12):
           return value
      else:
           raise ValidationError("Enter valid adhaar number")      

class CandidateForm(models.Model):
     GENDER=(
          ('MALE','MALE'),
          ('FEMALE','FEMALE'),
          ('OTHERS','OTHERS'),
     )
     MARTIAL_STATUS=(
          ('MARRIED','MARRIED'),
          ('UNMARRIED','UNMARRIED'),
     )
     appid=models.ForeignKey(User,on_delete=models.DO_NOTHING,unique=True)
     candidateName=models.CharField(max_length=50,null=True,blank=False)
     contactNo=models.CharField(max_length=10,validators=[validate_contactno],null=True,blank=False)
     dateOfBirth=models.DateField()
     gender=models.CharField(max_length=10,null=True,choices=GENDER,blank=False)
     fatherName=models.CharField(max_length=50,null=True,blank=False)
     foccupation=models.CharField(max_length=50,null=True,blank=False)
     motherName=models.CharField(max_length=50,null=True,blank=False)
     moccupation=models.CharField(max_length=50,null=True,blank=False)
     martialStat=models.CharField(max_length=10,null=True,blank=False,choices=MARTIAL_STATUS)
     AdhaarNo=models.CharField(max_length=12,null=True,blank=False,validators=[validate_Adhaarno])
     #p defines the permanent address
     phouseno=models.CharField(max_length=60,null=True,blank=False)
     pstreetcolony=models.CharField(max_length=100,null=True,blank=False)
     pstate=models.CharField(max_length=25,null=True,blank=False)
     ppincode=models.IntegerField(null=True,blank=False)
     #pre defines the present address
     prehouseno=models.CharField(max_length=60,null=True,blank=False)
     prestreetcolony=models.CharField(max_length=100,null=True,blank=False)
     prestate=models.CharField(max_length=25,null=True,blank=False)
     prepincode=models.IntegerField(null=True,blank=False)      

     def __str__(self):
          return self.candidateName


class EducationalDetailsForm(models.Model):
     BOARD=(
          ('CBSE','CBSE'),
          ('ICSE','ICSE'),
          ('STATE','STATE'),
          ('OTHERS','OTHERS'),
     )
     FINANCE=(
          ('Less than 1 lakh','Less than 1 lakh'),
          ('Less than 2.5 lakhs','Less than 2.5 lakhs'),
          ('Less than 10 lakhs','Less than 10 lakhs'),
          ('Greater than 10 lakhs','Greater than 10 lakhs'),
     )
     candidateId=models.ForeignKey(User,on_delete=models.DO_NOTHING,unique=True)
     tenthSchool=models.CharField(max_length=100,null=True,blank=False)
     tenthBoard=models.CharField(max_length=10,null=True,blank=False,choices=BOARD)
     tenthRollNo=models.IntegerField(null=True,blank=False)
     tenthPercent=models.FloatField(null=True,blank=False)
     clg12th=models.CharField(max_length=200,null=True,blank=False)
     clgBoard=models.CharField(max_length=200,null=True,blank=False)
     rollNo12th=models.IntegerField(null=True,blank=False)
     pecentage12th=models.FloatField(null=True,blank=False)
     emailid=models.EmailField(null=True,blank=False)
     annualIncome=models.CharField(max_length=50,null=True,blank=False,choices=FINANCE)

     def __str__(self):
          return self.candidateId.name
     

     
'''    
class CandidateDocs(models.Model):
     canid=models.ForeignKey(User,on_delete=models.DO_NOTHING,unique=True)
     candidatephoto=models.FileField(null=True)
     candidate10thMarksCard=models.FileField()
     candidate12thMarksCard=models.FileField()
     candidateIncomeCaste=models.FileField()
     candidates12thStudy=models.FileField() 

     def __str__(self):
          return self.canid.name   
'''          