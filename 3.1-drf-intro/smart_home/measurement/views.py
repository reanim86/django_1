
from rest_framework.response import Response

from .serializers import MeasurementSerializer, SensorDetailSerializer, SensorSerializer
from measurement.models import Measurement, Sensor
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView

class SensorAPI(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        sensor = Sensor(name=request.data['name'], description=request.data.get('description'))
        sensor.save()
        return Response('Record add')

class MeasurementAPI(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        measurement = Measurement(sensor_id=request.data['sensor'], temperature=request.data['temperature'])
        measurement.save()
        return Response('Record add')

class SensorDetail(APIView):
    def get(self, request, id):
        sensor = Sensor.objects.filter(id=id)
        ser = SensorDetailSerializer(sensor, many=True)
        return Response(ser.data)

    def patch(self, request, id):
        if request.data.get('name'):
            Sensor.objects.filter(id=id).update(name=request.data['name'])
        if request.data.get('description'):
            Sensor.objects.filter(id=id).update(description=request.data['description'])
        return Response('Record changed')
