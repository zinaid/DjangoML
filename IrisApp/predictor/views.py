from django.shortcuts import render
import pandas as pd
from django.http import JsonResponse
from .models import PredResults

def predictor(request):
    return render(request, 'predictor.html')

def predict_chances(request):

    if request.POST.get('action') == 'post':

        sepal_length = float(request.POST.get('sepal_length'))
        sepal_width = float(request.POST.get('sepal_width'))
        petal_length = float(request.POST.get('petal_length'))
        petal_width = float(request.POST.get('petal_width'))

        
        model = pd.read_pickle("KNN_model.pickle") 
       
        result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])

        classification = result[0]

        PredResults.objects.create(sepal_length=sepal_length, sepal_width=sepal_width, petal_length=petal_length,
                                   petal_width=petal_width, classification=classification)

        return JsonResponse({'result': classification, 'sepal_length': sepal_length,
                             'sepal_width': sepal_width, 'petal_length': petal_length, 'petal_width': petal_width},
                            safe=False)


def view_results(request):
    data = {"dataset": PredResults.objects.all()}
    return render(request, "db.html", data)