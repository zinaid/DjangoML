from django.shortcuts import render

def predictor(request):
    return render(request, 'predictor.html')
