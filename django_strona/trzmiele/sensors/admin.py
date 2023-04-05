from django.contrib import admin
from .models import Sensor, Measurement
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Sensor, BookAdmin)
admin.site.register(Measurement)