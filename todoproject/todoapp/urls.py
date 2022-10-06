from . import views
from django.urls import path
app_name = 'todoapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('delete/<int:task_id>/', views.delete, name='delete'),
    path('update/<int:task_id>/', views.update, name='update'),
    path('classhome/', views.TodoListview.as_view(), name='classhome'),
    path('classdetail/<int:pk>/', views.TodoDetailView.as_view(), name='classdetail'),
    path('classupdate/<int:pk>/',views.TodoUpdateView.as_view(), name='classupdate'),
    path('classdelete/<int:pk>/', views.TodoDeleteView.as_view(), name='classdelete')

]