from django.urls import path

from measurement.views import SensorAPI, MeasurementAPI, SensorDetail

urlpatterns = [
    path('sensors/', SensorAPI.as_view()),
    path('sensors/<int:id>/', SensorDetail.as_view()),
    path('measurements/', MeasurementAPI.as_view())
]
