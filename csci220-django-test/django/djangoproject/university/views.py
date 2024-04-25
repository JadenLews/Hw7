from django.shortcuts import render
from .models import Student
from .models import Guidance_Counselor
from .models import SupplementaryQuestion
from .models import Application
from .models import College

from itertools import groupby
from operator import attrgetter
# Create your views here.

def application_results(request):
    students = Student.objects.all().prefetch_related('application_set')
    return render(request, 'university/application_results.html', {'students': students})

def extracurriculars(request):
    students = Student.objects.all()

    for student in students:
        student.extracurriculars = {}
        participations = student.participates_in_set.all().order_by('extracurricular_name__extracurricular_type')

        for extracurricular_type, group in groupby(participations, key=attrgetter('extracurricular_name.extracurricular_type')):
            student.extracurriculars[extracurricular_type] = list(group)

    return render(request, 'university/extracurriculars.html', {'students': students})


def new_page(request):
    students = Student.objects.all()
    return render(request, 'university/new_page.html', {'students': students})


def guidance_page(request):
    counselors = Guidance_Counselor.objects.prefetch_related('student_set').all()
    return render(request, 'university/guidence_page.html', {'guidance': counselors})

def home(request):
    return render(request, 'university/home.html')

def instructions(request):
    return render(request, 'university/instructions.html')

def question_page(request):
    #questions = SupplementaryQuestion.objects.all()
    questions = SupplementaryQuestion.objects.prefetch_related('answers').all()
    return render(request, 'university/question_page.html', {'question': questions})

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
