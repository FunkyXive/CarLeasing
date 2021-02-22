from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Car)
admin.site.register(CarBrand)
admin.site.register(CarEquipment)
admin.site.register(Gearbox)
admin.site.register(Drivetrain)
admin.site.register(FuelType)
admin.site.register(CarModel)
admin.site.register(CarImage)
admin.site.register(Profile)
admin.site.register(Company)
admin.site.register(PrivateLease)
admin.site.register(CompanyLease)

