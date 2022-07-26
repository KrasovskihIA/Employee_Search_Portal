from django.shortcuts import render
from .models import *

#Все проекты
def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)


#Детальное представление
def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    return render(request, 'projects/single-projects.html', {'project': projectObj})
