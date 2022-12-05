from django.shortcuts import render, redirect
from .models import Project, Task
from .forms import CreateNewTask, CreateNewProject
from django.http import Http404

def index(request):
    title = "Course"
    return render(request, 'index.html', {
        'title': title
    })


def about(request):
    username = 'dayan'
    return render(request, 'about.html', {
        'username': username
    })


def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {
        'projects': projects
    })


def task(request):
    tasks = Task.objects.all()

    return render(request, 'tasks/tasks.html', {
            'tasks': tasks,
    })


def create_task(request):
    if request.method == 'GET':
        projects = Project.objects.all()
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask(),
            'projects': projects
        })
    else:

        id = Project.objects.get(name=request.POST['select']).id
        Task.objects.create(title=request.POST['title'],
                            description=request.POST['description'],
                            project_id=id)
        return redirect('tasks')


def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form': CreateNewProject()
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')


def project_detail(request, id):
    try:
        project = Project.objects.get(id=id)
        tasks = Task.objects.filter(project_id=id)
    except:
        raise Http404("Project not found")
    return render(request, 'projects/detail.html', {
        'project': project,
        'tasks': tasks
    })
