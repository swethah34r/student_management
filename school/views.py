from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from school.models import Students

# Create your views here.


@csrf_exempt
def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        standard = request.POST.get("standard")
        section = request.POST.get("section")

        Students.objects.create(
            name=name,
            age=age,
            standard=standard,
            section=section
        )

    return render(request, "index.html")


@csrf_exempt
def store_student(request):
    data = Students.objects.all()
    context = {"students": data}
    return render(request, "student_details.html", context)
