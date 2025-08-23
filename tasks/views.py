from django.shortcuts import render,redirect
from django.http import HttpResponse 
from tasks.forms import TaskFrom,TaskModelForm,TaskDetailModelform
from tasks.models import Employee,Task,TaskDetail, Project
from datetime import date
from django.db.models import Q, Count, Max, Min, Avg
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
# Create your views here.

def manager_dashbord(request):

    # count total task
    # total_task=Task.objects.all().count()
    # # pending task
    # completed_task=Task.objects.filter(status="COMPLETED").count()
    # # task in progres
    # in_progress_task=Task.objects.filter(status="IN_PROGRESS").count()
    # # todos
    # pending_task=Task.objects.filter(status="PENDING").count()
    
    # print(all)
    type=request.GET.get('type', 'all')
    
                    #   oneToone                  many to many 
    # tasks=Task.objects.select_related('details').prefetch_related('assigned_to').all()

    counts=Task.objects.aggregate(
        total_task=Count('id'),
        completed_task=Count('id',filter=Q(status="COMPLETED")),
        in_progress_task=Count('id',filter=Q(status="IN_PROGRESS")),
        pending_task=Count("id",filter=Q(status='PENDING')),
    )

    # retriving data 
    
    base_query=Task.objects.select_related('details').prefetch_related('assigned_to')
    if type=="completed_task":
         tasks =  base_query.filter(status="COMPLETED")
    elif type=="in_progress_task":
        tasks= base_query.filter(status="IN_PROGRESS")
    elif type=='pending_task':
        tasks= base_query.filter(status="PENDING")
    elif type=='all':
        tasks= base_query.all()
     
    context={
        "tasks":tasks,
        "counts":counts,
        
    }
    return render(request,"dashbord/manager_dashbord.html",context)

def user_dashbord(request):
    return render(request,"dashbord/user_dashbord.html")

def test(request):
    return render (request,'test.html')

def test1(request):

    names=["ruhul","sakib","siyem","raju","mubin","sakib"]
    count=0
    
    for name in names:
        count=count+1
    context={
        "names":names,
        "count":count,
    }
    return render (request,'test.html',context)




def test2(request):

    
    context={
         "names":["ruhul","sakib","siyem","raju","mubin","sakib"]
    }
    return render(request,'test.html',context)



def create_from(request):
    employees=Employee.objects.all()  #for GET
    # create from  ---->> froms.py
    task_form = TaskModelForm()
    task_details_form=TaskDetailModelform()

    if request.method == "POST":   
        task_form = TaskModelForm(request.POST)
        task_details_form=TaskDetailModelform(request.POST)

        if task_form.is_valid() and task_details_form.is_valid():
                
            """for model form data"""
            
            task=task_form.save() 
            task_details=task_details_form.save(commit=False)
            task_details.task=task
            task_details.save() 
            messages.success(request,"Task Create Successfully")
            return redirect('create_from')
            '''for django form data '''
            #    data=(form.cleaned_data)
            #    title=data.get('title')
            #    description=data.get('description')
            #    due_date=data.get('due_date')
            #    assigned_to=data.get('assigned_to')
            #    task=Task.objects.create(title=title,description=description,due_date=due_date)
            #    for emp_id in assigned_to:
            #        employee=Employee.objects.get(id=emp_id)
            #        task.assigned_to.add(employee)
         

    context={
    "task_form":task_form,
    "task_details_form":task_details_form,

    }
    return render(request,"task_from.html",context)





# update_task



def update_task(request, id):
    task=Task.objects.get(id=id)
    # create from  ---->> froms.py
    task_form = TaskModelForm(instance=task)
    if task.details:
         task_details_form=TaskDetailModelform(instance=task.details)

    if request.method == "POST":   
        task_form = TaskModelForm(request.POST,instance=task)
        task_details_form=TaskDetailModelform(request.POST,instance=task.details)

        if task_form.is_valid() and task_details_form.is_valid():
                
            """for model form data"""
            # update button thake jeita asbe oita asve korbe
            task_form=task_form.save()
            task_details=task_details_form.save(commit=False)
            task_details.task=task
            task_details.save() 
            messages.success(request,"Task Updated Successfully")
            return redirect('update_task',id)
            '''for django form data '''
            #    data=(form.cleaned_data)
            #    title=data.get('title')
            #    description=data.get('description')
            #    due_date=data.get('due_date')
            #    assigned_to=data.get('assigned_to')
            #    task=Task.objects.create(title=title,description=description,due_date=due_date)
            #    for emp_id in assigned_to:
            #        employee=Employee.objects.get(id=emp_id)
            #        task.assigned_to.add(employee)
         

    context={
    "task_form":task_form,
    "task_details_form":task_details_form,

    }
    return render(request,"task_from.html",context)


# delete task
def delete_task(request,id):
    if request.method == 'POST':
        task=Task.objects.get(id=id)
        
        task.delete()
        messages.success(request,'Task Delete Successfully')
        return redirect("manager-dashbord")
    else:
        messages.success(request,'Something Wrong')
        return redirect("manager-dashbord")








# databese thake data dakher jonno
 
def view_task(request):
     
    """jei task er ALL data dakte chai sei taks er name for emample"TASK" """
    # tasks=Task.objects.all()



    """secefic data dakte chaille bah retriv korte chaille""" 
    # tasks_3=Task.objects.get(pk=1)

    """first data dakte chaille """
    # first_task=Task.objects.first()
    """je kno ta ber korte chaille "filter" """
    # id=Task.objects.filter(id=1)
    """today data insert check"""
    # today=Task.objects.filter(due_date=date.today())

    """using and showing one to one and many to many/ForeignKey"""

    
    tasks=Task.objects.select_related('project').all()
    

    context = {
        "tasks":tasks
     
    }
    return render(request, "show_task.html", context)