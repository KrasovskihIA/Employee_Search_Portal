from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import ProjectForm



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


#Создание проекта
def createProject(request):
	form = ProjectForm()
	if request.method == 'POST':
		form = ProjectForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('projects')
	context = {'form': form}
	return render(request, 'projects/project_form.html', context)


#Редактирование проекта
def updateProject(request, pk):
	project = Project.objects.get(id=pk)
	form = ProjectForm(instance=project)
	if request.method == 'POST':
		form = ProjectForm(request.POST, instance=project)
		if form.is_valid():
			form.save()
			return redirect('projects')
	context = {'form': form}
	return render(request, 'projects/project_form.html', context)