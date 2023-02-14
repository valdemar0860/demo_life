from django.shortcuts import render, redirect
from django.views import generic
from .models import Task

import re

class TaskListView(generic.View):
    def get(self, request):
        # Task.objects.all().delete()
        permanent_tasks = Task.objects.filter(is_permanent=True)
        temporary_tasks = Task.objects.filter(is_permanent=False)
        if permanent_tasks.count() == 0:
            first_task_p = Task(title='perm', text='', is_permanent=True)
            first_task_p.save()
        if temporary_tasks.count() == 0:
            first_task_t = Task(title='temp', text='', is_permanent=False)
            first_task_t.save()
        context = {
            'permanent_tasks': permanent_tasks, 
            'temporary_tasks': temporary_tasks,
        }
        return render(request, 'tasks/daily_tasks.html', context)
    
    def post(self, request):
        permanent_tasks = Task.objects.filter(is_permanent=True)
        temporary_tasks = Task.objects.filter(is_permanent=False)
        #######################
        # check = temporary_tasks.get(id = 46)
        # check.is_completed = True
        # check.save()
        ################################
        task_title_pattern = re.compile(r'^title_\d+$')

        for field in request.POST:
            match_title = task_title_pattern.match(field) 
            if match_title:
                input_name = match_title.group(0)
                number = re.findall(r'[0-9]+', input_name)[0]
                new_task = request.POST.get(field)
                if new_task != '':
                    res = temporary_tasks.get(id = number)
                    res.title = new_task
                    res.save()   
        
        return redirect('task_list')       
                
        # context = {
        #     'permanent_tasks': permanent_tasks, 
        #     'temporary_tasks': temporary_tasks,
        # }
            
        # return render(request, 'tasks/daily_tasks.html', context)
    
    def autosave(request):
        if request.method == "POST":
            # input_data = request.POST.get("input_data")
            # Save the input data to the database
            # ...
            pass
            # return JsonResponse({"message": "Data saved successfully!"})
# from django.views import generic
# from django.shortcuts import render, redirect

# from .models import Task
# from datetime import date


# class TaskListView(generic.ListView):
#     model = Task
#     template_name = 'tasks/task.html'

#     def get_queryset(self):
#         permanent_tasks = Task.objects.filter(task_date__isnull=True)
#         temporary_tasks = Task.objects.exclude(task_date__isnull=True).filter(task_date__lt=date.today())
#         return permanent_tasks, temporary_tasks
    
#     def post(self, request):
#         if request.method == 'POST':
#             completed_task_ids = request.POST.getlist('completed_tasks')
#             for task_id in completed_task_ids:
#                 task = Task.objects.get(id=task_id)
#                 task.is_completed = True
#                 task.save()

#         new_task = request.POST.get('new_task')
#         if new_task:
#             Task.objects.create(title=new_task)

#         deleted_task_ids = request.POST.getlist('deleted_tasks')
#         for task_id in deleted_task_ids:
#             task = Task.objects.get(id=task_id)
#             task.delete()

#         edited_task_id = request.POST.get('edited_task_id')
#         if edited_task_id:
#             task = Task.objects.get(id=edited_task_id)
#             task.title = request.POST.get('edited_task_title')
#             task.save()

#         return redirect('task_list')