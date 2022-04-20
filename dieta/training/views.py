from django.shortcuts import render


def training(request):
    return render(request, 'training/training_form.html')