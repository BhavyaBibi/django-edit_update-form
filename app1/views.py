from django.shortcuts import render
from app1.models import StudentData

# Create your views here.


def HomePage(request):
    students = StudentData.objects.all()
    return render(request, 'homepage.html', {'students': students})


@csrf_exempt
def InsertStudent(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    gender = request.POST.get('gender')
    try:
        student = StudentData(name=name, email=email, gender=gender)
        student.save()
        stuent_data = {"id": student.id, "created_at": student.created_at,
                       "error": False, "errorMessage": "Student Added Successfully"}
        return JsonResponse(stuent_data, safe=False)

    except:
        stuent_data = {"error": True, "errorMessage": "Failed to Add Student"}
        return JsonResponse(stuent_data, safe=False)
