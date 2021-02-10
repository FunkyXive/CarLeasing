from django.db import models
from django.db.models import CharField, TextField, ManyToManyField, OneToOneField, ForeignKey, DateField, TimeField, DateTimeField, IntegerField, DecimalField, CASCADE
import datetime
from django.contrib.auth.models import User
# Create your models here.


class CarBrand(models.Model):
    brandName = CharField(max_length=50)

    def __str__(self):
        return self.brandName


class CarEquipment(models.Model):
    equipment = CharField(max_length=100)

    def __str__(self):
        return self.equipment


class Gearbox(models.Model):
    gearboxType = CharField(max_length=50)
    amountOfGears = IntegerField()

    def __str__(self):
        return f'{self.amountOfGears} Speed {self.gearboxType}'


class Drivetrain(models.Model):
    driveTrain = CharField(max_length=50)

<<<<<<< HEAD
=======
    def __str__(self):
        return self.driveTrain

>>>>>>> 59dae470433ab072cef4b54c09ba399a87064ef6

class FuelType(models.Model):
    fuelType = CharField(max_length=50, default='Gasoline')

<<<<<<< HEAD

class Company(models.Model):
    contactPerson = ForeignKey(User, on_delete=CASCADE)
    companyName = CharField(max_length=50)
    companyStreetName = CharField(max_length=100)
    companyStreetNumber = IntegerField()
    companyCity = CharField(max_length=20)
    companyPostalCode = IntegerField()
    cvrNumber = IntegerField(max)
=======
    def __str__(self):
        return self.fuelType
>>>>>>> 59dae470433ab072cef4b54c09ba399a87064ef6


class CarModel(models.Model):
    modelName = CharField(max_length=50)
    modelYear = IntegerField()
    modelBrand = ForeignKey(CarBrand, on_delete=CASCADE)
    modelFuelType = ForeignKey(FuelType, on_delete=CASCADE)
    modelPower = IntegerField()
    modelDriveTrain = ForeignKey(Drivetrain, on_delete=CASCADE)
    modelGearbox = ForeignKey(Gearbox, on_delete=CASCADE)
    modelEngineVolume = DecimalField(max_digits=2, decimal_places=1)
    modelEngineCylinders = IntegerField()

    def __str__(self):
        return f'{self.modelYear} {self.modelBrand} {self.modelName}'


class Car(models.Model):
    model = ForeignKey(CarModel, on_delete=CASCADE)
    milage = IntegerField()
    equipment = ManyToManyField(CarEquipment)
<<<<<<< HEAD
    carCurrentlyLeased = models.BooleanField(default=False)


class PrivateLease(models.Model):
    leaseStartDate = DateField()
    leaseEndDate = DateField()
    leaseDownpayment = DecimalField(max_digits=10, decimal_places=2)
    leaseMonthlyPrice = DecimalField(max_digits=10, decimal_places=2)
    leaseCar = OneToOneField(Car, on_delete=CASCADE)
    leaseCustomer = ForeignKey(User, on_delete=CASCADE)


class CompanyLease(models.Model):
    leaseStartDate = DateField()
    leaseEndDate = DateField()
    leaseDownpayment = DecimalField(max_digits=10, decimal_places=2)
    leaseMonthlyPrice = DecimalField(max_digits=10, decimal_places=2)
    leaseCar = OneToOneField(Car, on_delete=CASCADE)
    leaseCustomerCompany = ForeignKey(Company, on_delete=CASCADE)

    
#class Contract(moodels.Model):
#    contract = models.FileField() //todo
=======

    def __str__(self):
        return f'{self.model}'
>>>>>>> 59dae470433ab072cef4b54c09ba399a87064ef6
