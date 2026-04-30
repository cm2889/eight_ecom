from django.shortcuts import render

# Create your views here.


def ecom_dashboard (request):
     return render(request, 'home/home.html')