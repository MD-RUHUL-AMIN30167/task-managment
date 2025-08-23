
from django.urls import path
from .views import manager_dashbord, user_dashbord, test,test1,test2,create_from,view_task,update_task,delete_task

urlpatterns =[
    
    path('manager_dashbord/', manager_dashbord, name="manager-dashbord"),
    path('user_dashbord/', user_dashbord),
    path('test/', test),
    path('test1/',test1),
    path('test2/',test2),
    path('create_from/',create_from,name="create_from"),
    path('view_task/',view_task),
    path('update_task/<int:id>/',update_task,name='update_task'),
    path('delete_task/<int:id>/',delete_task,name='delete_task'),
]



 

