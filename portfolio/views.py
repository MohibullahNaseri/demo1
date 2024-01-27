from django.shortcuts import render
from .models import Portfolio
# Create your views here.
def about(request):
    return render(request, 'about.html')
def projects(request):
    return render(request, 'projects.html')

def portfolio(request):
    s1 = Portfolio()
    s1.name_s = 'HTML'
    s1.per = 100
    s2 = Portfolio()
    s2.name_s = 'CSS'
    s2.per = 70
    s3 = Portfolio()
    s3.name_s = 'JAVASCRIPT'
    s3.per = 60
    s4 = Portfolio()
    s4.name_s = 'DJANGO'
    s4.per = 40
    s5 = Portfolio()
    s5.name_s = 'PYTHON'
    s5.per = 70

    p1 = Portfolio()
    p1.name_p = 'APP DEV'
    p1.dec = 'Weather application which shows weather condition around the globe'
    p2= Portfolio()
    p2.name_p = 'WEB DEV'
    p2.dec = 'A simple web page of portfolio'

    skills = [s1, s2, s3, s4, s5]
    projects = [p1 ,p2]

    return render(request, 'demo.html', {'skills': skills, 'projects': projects})