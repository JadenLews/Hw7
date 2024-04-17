from django.shortcuts import render
from .models import Student
# Create your views here.
def new_page(request):
    students = Student.objects.all() 
    return render(request, 'university/new_page.html', {'students': students})