# models.py

from django.db import models

class Employ(models.Model):
    # image = models.ImageField(upload_to='employe_images/', default='jpg/')
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='employe_images/')
    phone = models.CharField(max_length=12)
    join_date = models.DateField(null=True, blank=False)
    email= models.EmailField()
    developer = [
    ('frontend Developer', 'frontend Developer'),
    ('backend Developer', 'backend Developer'),
    ('java Developer','java Developer'),
    ('Python Developer','Python Developer'),
    ('php Developer','php Developer'),
    ('graphic designer', 'graphic designer'),
    ('fullstack Developer','fullstack Developer'),
    ('Technical Leader','Technical Leader'),
    ('Associate Software Engineer','Associate Software Engineer'),
    ('Consulting python Developer','Consulting python Developer'),
    ('Junior Software Engineer','Junior Software Engineer'),
    ('Senior Ui/Ux Designer','Senior Ui/Ux Designer'),
     ('Technical Director','Technical Director'),
  ]
    developer= models.CharField(max_length=50, choices=developer,)
    def __str__(self):
        return self.name
    
class Task(models.Model):
    
    task = models.CharField(max_length=100)
    due_date = models.DateField()
    priority_choices = [
    ('Low', 'Low'),
    ('Medium', 'Medium'),
    ('High', 'High'),
  ]
    priority= models.CharField(max_length=6, choices=priority_choices, default='Low') #new field
    employ = models.ManyToManyField(Employ)  # all data in the print taxt_from list in the page 
    # employee = models.ForeignKey(Employee, on_delete=models.PROTECT) foreignkey in one value in the select in the database in the 
    def __str__(self):
        return self.task
    
class Leave(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    employ = models.ForeignKey('Employ', on_delete=models.CASCADE)
    start_date = models.DateField(null=True, blank=False)
    start_time = models.TimeField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=False)
    end_time = models.TimeField(null=True, blank=False)
    reason = models.TextField()
    

    def __str__(self):
        return f"{self.employ.name} - {self.status}"
