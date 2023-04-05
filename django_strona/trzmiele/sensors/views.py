import json
from django.shortcuts import render
from .models import Sensor, Measurement
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def home(request):
    sensors = Sensor.objects.all()
    if request.method == "POST":
        id = int(request.POST.get("id"))
        value = float(request.POST.get("measurement"))
        unit=request.POST.get("unit")
        sensor = Sensor.objects.get(id=request.POST.get("id"))
        measurement = Measurement.objects.create(
            sensor_id=sensor,
            value=value,
            unit=unit
        )

    context = {
        "sensors":sensors
        }
    return render(request, "sensors/home.html", context)

def sensorPage(request, pk):
    sensor = Sensor.objects.get(id=pk)
    print(sensor.name)
    try:
        measurement = sensor.measurement_set.all()[0]
    except:
        print("brak pomiarow")
        measurement = 0
    photo = "sensors/{}.jpg".format(sensor.id)

    context = {"sensor":sensor, "measurement":measurement, "photo":photo}
    return render(request, "sensors/sensorPage.html", context)

def ciekawostki(request):
    return render(request, "sensors/ciekawostki.html")

def onas(request):
    return render(request, "sensors/o_nas.html")
