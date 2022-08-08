from django.shortcuts import render
from app1.models import StudentData

# Create your views here.


def HomePage(request):
    students = StudentData.objects.all()
    return render(request, 'homepage.html', {'students': students})
