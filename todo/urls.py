from django.urls import path


from .views  import todoView ,addTodo , deletetodo
app_name = 'todo'
urlpatterns = [
    path('',todoView),
    path('addTodo',addTodo),
    path('deletetodo/<int:todo_id>',deletetodo),



]
