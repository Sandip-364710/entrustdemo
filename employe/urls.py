
from django.urls import path
from .views import (
    RedirectViewExample,
    TemplateViewExample,
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    SignupView,
    UserLoginView,
    UserLogoutView,
     LeaveListView, LeaveCreateView,LeaveDetailView
)
from .views import EmployListView, EmployDetailView, EmployCreateView, EmployUpdateView, EmployDeleteView,Homeviews
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("", Homeviews.as_view(), name="home"),
    # path('', RedirectViewExample.as_view(), name='redirect_view'),
    path('dashboard/', TemplateViewExample.as_view(), name='dashboard'),
    path('tasks/', TaskListView.as_view(), name='task_list'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('tasks/create/', TaskCreateView.as_view(), name='task_create'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
#    employ detail
    path('employ/', EmployListView.as_view(), name='employ_list'),
    path('employ/<int:pk>/', EmployDetailView.as_view(), name='employ_detail'),
    path('employ/create/', EmployCreateView.as_view(), name='employ_create'),
    path('employ/update/<int:pk>/', EmployUpdateView.as_view(), name='employ_update'),
    path('employ/delete/<int:pk>/', EmployDeleteView.as_view(), name='employ_delete'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('leaves/', LeaveListView.as_view(), name='leave-list'),
    path('leave_form/', LeaveCreateView.as_view(), name='leave-apply'),
    path('leave/<int:pk>/', LeaveDetailView.as_view(), name='leave_detail'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)