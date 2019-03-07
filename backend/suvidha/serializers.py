# todo/serializers.py

from rest_framework import serializers
from .models import Aircraft

class AircraftSerializer(serializers.ModelSerializer):
  class Meta:
    model = Aircraft
    fields = ('id','msn','harness_length','atmos_pressure','room_temperature','dep_airport','arr_airport','halt_airport','dep_date','arr_date', 'fuel_capacity_left_wing','fuel_capacity_right_wing','fuel_quantity_left_wing','fuel_quantity_right_wing','max_altitude_reached','flight_number','gross_weight','remark', 'flight_good_condition')