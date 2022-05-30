from django.urls import path
from .import views

app_name = 'predictor'

urlpatterns = [
    path('', views.predictor, name = 'predictor'),
]
