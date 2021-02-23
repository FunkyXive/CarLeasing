from django.db import models
from django.db.models import CharField, TextField, ManyToManyField, OneToOneField, ForeignKey, DateField, TimeField, DateTimeField, IntegerField, DecimalField, CASCADE
import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.


class Profile(models.Model):
    profileUser = OneToOneField(User, on_delete=CASCADE)
    profilePhoneNumber = DecimalField(decimal_places=0, max_digits=8)
    profileCprNumber = DecimalField(max_digits=10, decimal_places=0)
    profileAddress = CharField(max_length=100)
    profileCity = CharField(max_length=50)
    profilePostalCode = IntegerField()

    def __str__(self):
        return f"{self.profileUser}"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(profileUser=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


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
        return f'{self.amountOfGears}-Speed {self.gearboxType}'


class Drivetrain(models.Model):
    driveTrain = CharField(max_length=50)

    def __str__(self):
        return self.driveTrain


class FuelType(models.Model):
    fuelType = CharField(max_length=50, default='Gasoline')

    def __str__(self):
        return self.fuelType


class Company(models.Model):
    contactPerson = ForeignKey(User, on_delete=CASCADE)
    companyName = CharField(max_length=50)
    companyAddress = CharField(max_length=100)
    companyCity = CharField(max_length=20)
    companyPostalCode = IntegerField()
    cvrNumber = IntegerField()

    def __str__(self):
        return f"{self.companyName}"


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


class CarImage(models.Model):
    image = models.ImageField(upload_to='cars')

    def __str__(self):
        return self.image.url


class Car(models.Model):
    model = ForeignKey(CarModel, on_delete=CASCADE)
    milage = IntegerField()
    equipment = ManyToManyField(CarEquipment)
    carCurrentlyLeased = models.BooleanField(default=False)
    carImage = ManyToManyField(CarImage)
    carNewPrice = IntegerField(default=1)

    def __str__(self):
        return f'{self.model}'


class PrivateLease(models.Model):
    leaseStartDate = DateField()
    leaseEndDate = DateField()
    leaseDownpayment = DecimalField(max_digits=10, decimal_places=2)
    leaseMonthlyPrice = DecimalField(max_digits=10, decimal_places=2)
    leaseCar = OneToOneField(Car, on_delete=CASCADE)
    leaseCustomer = ForeignKey(User, on_delete=CASCADE)
    leaseMilesPerYear = IntegerField()
    contract = models.FileField(upload_to="contracts")

    def __str__(self):
        return f"{self.leaseCustomer} {self.leaseCar}"


class CompanyLease(models.Model):
    leaseStartDate = DateField()
    leaseEndDate = DateField()
    leaseDownpayment = DecimalField(max_digits=10, decimal_places=2)
    leaseMonthlyPrice = DecimalField(max_digits=10, decimal_places=2)
    leaseCar = OneToOneField(Car, on_delete=CASCADE)
    leaseCustomerCompany = ForeignKey(Company, on_delete=CASCADE)
    leaseMilesPerYear = IntegerField()
    contract = models.FileField(upload_to="contracts")

    def __str__(self):
        return f"{self.leaseCustomerCompany} {self.leaseCar}"
# class Contract(moodels.Model):
#    contract = models.FileField() //todo
