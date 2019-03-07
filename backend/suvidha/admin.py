from django.contrib import admin

from .models import Aircraft # add this

class SuvidhaAdmin(admin.ModelAdmin):  # add this
  list_display = ('msn', 'harness_length', 'gross_weight','flight_number','atmos_pressure','room_temperature','arr_airport','dep_airport', 'halt_airport','dep_date','arr_date','fuel_capacity_left_wing','fuel_capacity_right_wing','fuel_quantity_left_wing','fuel_quantity_right_wing') # add this

# Register your models here.
admin.site.register(Aircraft, SuvidhaAdmin) # add this