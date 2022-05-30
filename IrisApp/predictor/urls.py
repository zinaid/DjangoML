from django.urls import path
from .import views

app_name = 'predictor'

urlpatterns = [
    path('', views.predictor, name = 'predictor'),
    path('predict/', views.predict_chances, name = 'submit_prediction'),
    path('results/', views.view_results, name='results'),
]
