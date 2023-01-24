from django.urls import path

from measurement.views import SensorAPI, MeasurementAPI

urlpatterns = [
    path('sensors/', SensorAPI.as_view()),
    path('sensors/<int:id>/', SensorAPI.as_view()),
    path('measurements/', MeasurementAPI.as_view())
]
