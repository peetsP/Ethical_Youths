from django.shortcuts import render
from .models import TopCarousel

# Create your views here.

def index(request):

    carousels = TopCarousel.objects.all()

    context = {'carousels': carousels}

    return render(request, 'index.html', context=context)