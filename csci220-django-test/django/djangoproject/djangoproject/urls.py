"""djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path
#from university.views import new_page
from university.views import guidance_page
from university.views import home
from university.views import instructions
from university.views import question_page
from university.views import application_results
from university.views import college_page
from university.views import extracurriculars
from university.views import home_page


urlpatterns = [
    path('', lambda req: redirect('home/')),
    path('minifacebook/', include('minifacebook.urls')),
    path('admin/', admin.site.urls),
    path('guidance_page/', guidance_page, name='guidance_page'),
    path('home/', home, name='home'),
    path('instructions/', instructions, name='instructions'),
    path('question_page/', question_page, name='question_page'),
    path('application_results/', application_results, name='application_results'),
    path('college-page/', college_page, name="college_page"),
    path('extracurriculars/', extracurriculars, name="extracurriculars")
    #path('home-page/', home_page, name='home_page'),
]


