
from rest_framework.response import Response

from .serializers import MeasurementSerializer, SensorDetailSerializer
from measurement.models import Measurement, Sensor
from rest_framework.generics import ListAPIView

class SensorAPI(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def post(self, request):
        sensor = Sensor(name=request.data['name'], description=request.data.get('description'))
        sensor.save()
        return Response('Record add')

    def patch(self, request, id):
        if request.data.get('name'):
            Sensor.objects.filter(id=id).update(name=request.data['name'])
        if request.data.get('description'):
            Sensor.objects.filter(id=id).update(description=request.data['description'])
        return Response('Record changed')

class MeasurementAPI(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
