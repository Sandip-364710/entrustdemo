# views.py
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import RedirectView, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.forms import UserCreationForm 
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Task
from .models import Employ,Leave

class RedirectViewExample(RedirectView):
    url = '/dashboard/'

class TemplateViewExample(TemplateView):
    template_name = 'welcome.html'

class TaskListView(LoginRequiredMixin,ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'

class TaskCreateView(CreateView):
    model = Task
    template_name = 'task_form.html'
    fields = ['task', 'due_date', 'priority' ,'employ']
    success_url = reverse_lazy('task_list')
    def form_valid(self, form):
        messages.success(self.request, ' Task-Created Successfully')  # Add success message
        return super().form_valid(form) 

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'task_form.html'
    fields = ['task', 'due_date', 'priority','employ']
    success_url = reverse_lazy('task_list')
    def form_valid(self, form):
        messages.success(self.request, 'Task-Updated successfully')  # Add success message
        return super().form_valid(form) 

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_confirm_delete.html'
    success_url = reverse_lazy('task_list')

    
# employ
    
class EmployListView(LoginRequiredMixin,ListView):
    model = Employ
    template_name = 'employ_list.html'
    context_object_name = 'employs'

class EmployDetailView(DetailView):
    model = Employ
    template_name = 'employ_detail.html'
    context_object_name = 'employ'


class EmployCreateView(CreateView):
    model = Employ
    template_name = 'employ_form.html'
    fields = ['image','name', 'phone','developer','join_date','email']
    success_url = reverse_lazy('employ_list')
    def form_valid(self, form):
        messages.success(self.request, 'Employee-Created successfully')  # Add success message
        return super().form_valid(form) 


class EmployUpdateView(UpdateView):
    model = Employ
    template_name = 'employ_form.html'
    fields = ['image','name', 'phone', 'developer','join_date','email']
    success_url = reverse_lazy('employ_list')
    def form_valid(self, form):
         messages.success(self.request, ' Employee Updated  successfully')  # Add success message
         return super().form_valid(form) 

class EmployDeleteView(DeleteView):
    model = Employ
    template_name = 'employ_confirm_delete.html'
    success_url = reverse_lazy('employ_list')


class Homeviews(TemplateView):
    template_name='home.html'


# signup
    

class SignupView(CreateView):
    template_name = 'signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    def form_valid(self, form):
         messages.success(self.request, 'Thanks for Signup')  # Add success message
         return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = 'login.html'
    def form_valid(self, form):
         messages.success(self.request, 'Thanks for Login ')  # Add success message
         return super().form_valid(form)


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home')
    
    
    
    
class LeaveListView(LoginRequiredMixin,ListView):
    model = Leave
    template_name = 'leave_list.html'
    context_object_name = 'leaves'

class LeaveCreateView(LoginRequiredMixin,CreateView):
     model = Leave
     fields = ['employ', 'start_date', 'end_date', 'reason','start_time','end_time']
     template_name = 'leave_form.html'  # Template for the leave creation form 
     success_url = '/leaves/'
    #  def form_valid(self, form):
    #     messages.success(self.request, ' Leave ')  # Add success message
    #     return super().form_valid(form) 


class LeaveDetailView(DetailView):
    model = Leave
    template_name = 'leave_detail.html'
    context_object_name = 'leave'