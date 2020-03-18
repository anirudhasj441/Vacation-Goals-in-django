from django.shortcuts import render
from .models import Goals
# Create your views here.
def index(request):
    goals = Goals.objects.all()
    params = {
        'goals':goals,
    }
    return render(request,'app/index.html',params)