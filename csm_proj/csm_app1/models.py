from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Registration(models.Model):
    #user=models.OneToOneField(User, on_delete=models.CASCADE)
    fullname=models.CharField( max_length=250)
    address=models.CharField(max_length=250)
    email=models.EmailField()
    phno=models.CharField(max_length=15)
    citylist=(
        ('Bengaluru','Bengaluru'),
        ('Dharwad','Dharwad'),
        ('Hubballi','Hubballi'),
        ('Bagalkot','Bagalkot'),
        ('Ballari','Ballari'),
        ('Chikkaballapur','Chikkaballapur'),
        ('Davanagere','Davanagere'),
        ('Gadag','Gadag'),
        ('Gulbarga','Gulbarga'),
        ('Hassan','Hassan'),
        ('Haveri','Haveri'),
        ('Hospet','Hospet'),
        ('Koppal','Koppal'),
        ('Mysore','Mysore'),
        ('Mysore','Mysore'),
        ('Raichur','Raichur'),
        ('Shimoga','Shimoga'),
        ('Udupi','Udupi'),
        ('Yellapur','Yellapur'),
    )
    city=models.CharField(max_length=100,choices=citylist)
    pincode=models.IntegerField()
    regno=models.CharField( max_length=10)
    owner=models.CharField(max_length=200)
    model=models.CharField(max_length=50)
    fueltype=(('Petrol','Petrol'),('Diesel','Diesel'),('CNG','CNG'),('Bio-Diesel','Bio-Diesel'),)
    fuel=models.CharField(choices=fueltype, max_length=50)
    colour=models.CharField(max_length=15)
    expdate=models.DateField(blank=True)
    deltype=(('Delivery Type','Delivery Type'),('Pickup Service','Pickup Service'),('Drop Service','Drop Service')   )
    delivery=models.CharField(choices=deltype, max_length=50, )
    servdate=models.DateField(blank=True)
    pickdate=models.DateField(blank=True)
    servtype=(('General Service','General Service'), ('Fuel Service','Fuel Service'), ('Interim Service','Interim Service'),   ('Battery Check and Service','Battery Check and Service'),  ('Full Car Service','Full Car Service'), ('Denting and Painting','Denting and Painting'), ('Major Car Service','Major Car Service'),('Accidental Repairs','Accidental Repairs') )
    serv=models.CharField(max_length=50, choices=servtype)
    othserv=(('Tyre Replace','Tyre Replace') , ('Sparkplug, Clutch and Brake Service','Sparkplug, Clutch and Brake Service'),
    ('Windshield Replace','Windshield Replace'),
    ('Engine Replace','Engine Replace'),
    ('AC service and Replace','AC service and Replace'),
    ('Car Wash','Car Wash'),
    ('Interior Cleaning','Interior Cleaning'),
    ('Car Heater Service','Car Heater Service'),
    ('Oil Replace','Oil Replace'),
    ('Other/Custom Service','Other/Custom Service') )
    oth=models.CharField(choices=othserv,max_length=40)


    '''@receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Registration.objects.create(user=instance)'''

    
