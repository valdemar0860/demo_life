from django.shortcuts import redirect
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

from .models import Task

import re


class TaskListView(generic.ListView):
    template_name = 'tasks/task.html'
    model = Task

    @csrf_exempt
    def post(self, request):
        if request.method == 'POST':
            tasks = Task.objects.all()

            task_title_pattern = re.compile(r'^title_\d+$')
            task_checkbox_pattern = re.compile(r'^checkbox_\d+$')

            for field in request.POST:
                # if the user changes the text in the input field,
                # we find the id of the element for which the title was changed
                # and apply the changes in the database
                match_title = task_title_pattern.match(field)
                if match_title:
                    input_name = match_title.group(0)
                    input_number = re.findall(r'[0-9]+', input_name)[0]
                    new_task = request.POST.get(field)
                    if new_task != '':
                        res_title = tasks.get(id=input_number)
                        res_title.title = new_task
                        res_title.save()

                # if the user puts a check mark next to some checkbox,
                # it means that the user has completed some task,
                # and we also apply these changes to the database
                match_checkbox = task_checkbox_pattern.match(field)
                if match_checkbox:
                    check_item = match_checkbox.group(0)
                    check_number = re.findall(r'[0-9]+', check_item)[0]
                    print(check_number)
                    res_check = tasks.get(id=check_number)
                    res_check.is_completed = True
                    res_check.save()

            # return JsonResponse({'success': True})
            return redirect('task_list')
        # return JsonResponse({'success': False})
        return redirect('task_list')


