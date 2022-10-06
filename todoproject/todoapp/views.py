from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .form import ToDoForm
from .models import ToDo
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
# Create your views here.


def home(request):
    return render(request, 'home.html')


class TodoListview(ListView):
    model = ToDo
    template_name = 'classhome.html'
    context_object_name = 'tasks'


class TodoDetailView(DetailView):
    model = ToDo
    template_name = 'detail.html'
    context_object_name = 'task'


class TodoUpdateView(UpdateView):
    model = ToDo
    template_name = 'classupdate.html'
    context_object_name = 'task'
    fields = ('title','priority','date')

    def get_success_url(self):
        return reverse_lazy('todoapp:classdetail', kwargs={'pk': self.object.id})


class TodoDeleteView(DeleteView):
    model = ToDo
    template_name = 'delete_task.html'
    success_url = reverse_lazy('todoapp:classhome')


def add(request):
    task_list = ToDo.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        priority = request.POST.get('priority')
        date = request.POST.get('date')
        task = ToDo(title=title, priority=priority, date=date)
        task.save()
    return render(request, 'add_task.html', {'tasks': task_list})


def update(request,task_id):
    tasks = ToDo.objects.get(id=task_id)
    form_value = ToDoForm(request.POST or None, instance=tasks)
    if form_value.is_valid():
        form_value.save()
        return redirect('todoapp:add')
    return render(request, 'edit_task.html', {'form': form_value, 'task': tasks})


def delete(request, task_id):
    if request.method == 'POST':
        task_ids = ToDo.objects.get(id=task_id)
        task_ids.delete()
        return redirect('todoapp:add')
    return render(request, 'delete_task.html')