from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PictureForm
from bc_mod.breast_cancer import predict_accuracy, predict_class, get_model



def index(request):
    
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            test_img = form.cleaned_data['picture']
            form_save = form.save()
            classes = 5
            accuracy = 5
            get_model()
            classes = predict_class(test_img)
            accuracy = predict_accuracy(test_img)
                
    else:
        classes = 5
        accuracy = 5
        form = PictureForm()
    return render(request,'app/index.html',{'form': form, 'classes': classes,'accuracy': accuracy})

