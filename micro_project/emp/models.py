from django.db import models
from PIL import Image
from django.utils import timezone

# Create your models here.
divi=[('Dhaka','Dhaka'),('Rajshahi','Rajshahi'),('Sylhet','Sylhet'),
      ('Khulna','Khulna'),('Barishal','Barishal'),('Dinajpure','Dinajpure'),
      ('Mymanshingho','Mymanshigho')]

gen=[('Male','male'),
     ('Female','female')]

mari_status=[('Married','married'),
             ('Single','single')]


class Locations(models.Model):
    loc_id=models.AutoField(primary_key=True)
    loc_city=models.CharField(max_length=40,blank=True)
    loc_district=models.CharField(max_length=25,blank=True)
    loc_division=models.CharField(max_length=13,blank=True,choices=divi,default='Dha')

    def __str__(self):
        return self.loc_city

    class Meta:
        db_table = 'LOCATIONS'
        ordering = ['loc_id']
        permissions = [
            ('add_loc', 'can add locations')
        ]


class Branches(models.Model):
    bran_id=models.AutoField(primary_key=True)
    bran_name=models.CharField(max_length=25,blank=True)

    bran_address=models.CharField(max_length=100,blank=True)

    bran_location=models.ForeignKey(Locations,on_delete=models.CASCADE,null=True,
                                    )

    def __str__(self):
        return self.bran_name

    def Modify(self):
        loc=Locations.objects.raw('SELECT loc_id,loc_city FROM locations')
        self.bran_location=loc

    class Meta:
        db_table='BRANCHES'
        ordering=['bran_id']
        permissions=[
            ('add_bran','can add branch')
        ]

class Jobs(models.Model):
    job_id=models.AutoField(primary_key=True)
    job_name=models.CharField(max_length=30,blank=True)
    max_salary=models.IntegerField(blank=True)
    mini_salary=models.IntegerField(blank=True)

    def __str__(self):
        return self.job_name


    class Meta:
        db_table='JOBS'
        ordering=['job_id']


class Emp(models.Model):
    emp_id=models.CharField(primary_key=True,max_length=10)
    emp_first_name=models.CharField(max_length=20,null=False)
    emp_last_name=models.CharField(max_length=20,null=False)
    emp_father_name=models.CharField(max_length=15,blank=False,default='')
    emp_mother_name=models.CharField(max_length=15,blank=False,default='')
    emp_married=models.CharField(max_length=8,blank=False,choices=mari_status,default='Single')
    emp_address=models.TextField(null=False)
    emp_gender= models.CharField(max_length=6,blank=False,choices=gen,default='male')
    emp_phone=models.IntegerField(blank=True,null=True)
    emp_email=models.EmailField(blank=True,null=True)
    emp_bod=models.DateField()
    emp_salary=models.IntegerField(null=False)
    emp_blood=models.CharField(max_length=4)
    emp_manager=models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True)
    emp_job=models.ForeignKey(Jobs,on_delete=models.CASCADE,null=True,
                              )
    emp_branch=models.ForeignKey(Branches,on_delete=models.CASCADE,null=True,blank=True
                                 )
    emp_photo=models.ImageField(blank=True,upload_to='static/image/emp',)


    def __str__(self):
        return  (self.emp_first_name+' '+self.emp_last_name)



    def Modify(self):
        j=Jobs.objects.raw('SELECT job_id,job_name FROM jobs')
        self.emp_job=j
        b=Branches.objects.raw('SELECT bran_id,bran_name FROM branches')
        self.emp_branch=b

    def save(self):
        super().save()
        img=Image.open(self.emp_photo.path)
        if img.height>200 or img.width>150:
            output_size=(150,150)
            img.thumbnail(output_size)
            img.save(self.emp_photo.path)




    class Meta:
        db_table='EMPLOYEES'
        ordering=['emp_id']
        permissions=[
            ('add_employee','can add employees')
        ]