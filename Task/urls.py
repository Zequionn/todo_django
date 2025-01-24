from django.urls import path
from . import views

urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
    path('markTaskasDone/<int:pk>', views.markTaskAsDoneOrUndone, name='markTaskAsDoneOrUndone'),
    path('delete_task/<int:pk>', views.deteleTask, name='delete_task'),
    path('edit_task/<int:pk>', views.edit_task, name='edit_task')

]
