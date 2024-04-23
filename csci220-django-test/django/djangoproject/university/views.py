from django.shortcuts import render
from .models import Student
# Create your views here.
def new_page(request):
    students = Student.objects.all() 
    return render(request, 'university/new_page.html', {'students': students})

def college_page(request):
    colleges = College.objects.all()
    for college in colleges:
        college.total_count = Application.objects.count()
        college.admitted_count = Application.objects.filter(app_status='admitted').count()
        if college.total_count > 0:
            college.acceptance_rate = (college.admitted_count / college.total_count * 100)
        else: 
            college.acceptance_rate = "No application records found."
    return render(request, 'university/college_page.html', {'colleges': colleges})

def home_page(request):
    return render(request, 'university/home_page.html')
