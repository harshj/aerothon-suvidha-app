from django.db import models

# Create your models here.
class Aircraft(models.Model):
      msn = models.CharField(max_length=120)
      harness_length = models.IntegerField()
      atmos_pressure = models.IntegerField()
      room_temperature = models.IntegerField()
      dep_date=models.CharField(max_length=120,default=0)
      arr_date=models.CharField(max_length=120,default=0)
      dep_airport=models.CharField(max_length=150,default="DEL")
      arr_airport=models.CharField(max_length=150,default="BLR")
      halt_airport=models.CharField(max_length=150,default="NULL")
      fuel_capacity_left_wing = models.IntegerField()
      fuel_capacity_right_wing = models.IntegerField()
      fuel_quantity_left_wing = models.IntegerField()
      fuel_quantity_right_wing = models.IntegerField()
      max_altitude_reached = models.IntegerField()
      flight_number = models.CharField(max_length=10)
      gross_weight = models.IntegerField()
      remark = models.TextField()
      flight_good_condition = models.BooleanField(default=True)

      def _str_(self):
        return self.msn
