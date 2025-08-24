from django.contrib import admin
from django.urls import path,include
from debug_toolbar.toolbar import debug_toolbar_urls
from django.http import HttpResponse
def home(request):
    return HttpResponse("<h1>Welcome to Task Management</h1>")
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("tasks/",include("tasks.urls")),  
    

]+debug_toolbar_urls()

