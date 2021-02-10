from django.db import models
from django.db.models import CharField, TextField, ManyToManyField, OneToOneField, ForeignKey, DateField, TimeField, DateTimeField, IntegerField, DecimalField, CASCADE
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

    def __str__(self):
        return self.driveTrain


class FuelType(models.Model):
    fuelType = CharField(max_length=50, default='Gasoline')

    def __str__(self):
        return self.fuelType


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

    def __str__(self):
        return f'{self.model}'
