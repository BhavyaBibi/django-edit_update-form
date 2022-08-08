from django.http import HttpResponse
from django.test import TestCase
from django.http import HttpResponse

# Create your tests here.
def HomePage(request):
    return HttpResponse('home')
