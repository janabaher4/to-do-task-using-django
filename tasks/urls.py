from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='tasks/login.html'), name='login'),  # Use the built-in LoginView # type: ignore
    path('logout/', views.logout_view, name='logout'),  # Use the built-in LogoutView # type: ignore
    path('create/', views.task_create, name='task_create'),
    path('', views.task_list, name='task_list'),
    path('<int:pk>/edit/', views.task_edit, name='task_edit'),
    path('<int:pk>/delete/', views.task_delete, name='task_delete'),
]
