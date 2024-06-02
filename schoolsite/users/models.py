from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import *


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        STUDENT = "STUDENT", "Student"
        TEACHER = "TEACHER", "Teacher"

    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices)
    dob = models.DateField(("Date of Birth"), default=date.today)
    admin_image = models.ImageField(default='admin_default.jpg', upload_to='admin_pictures')


    @property
    def age(self):
        today = date.today()
        age =(today - self.dob)
        return age
    

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)

class StudentManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.STUDENT)

class Student(User):
    base_role = User.Role.STUDENT
    student = StudentManager()
    class Meta:
        proxy = True
     
class StudentMarks(models.Model):
    st_mk = models.ForeignKey(Student, on_delete=models.CASCADE)
    English = models.IntegerField( default=0)
    Hindi = models.IntegerField( default=0)
    Marathi = models.IntegerField( default=0)
    Maths = models.IntegerField(default=0)
    Science = models.IntegerField( default=0)
    Total = models.IntegerField(default=0)

    def __str__(self):
        return str(self.st_mk.username)

class StudentCompetition(models.Model):
    comp = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null =True )
    sport = models.CharField(max_length=20, default=None)
    sport_desc = models.TextField(max_length=1000, default='desc')
    sport_image = models.ImageField(default='default.jpg', upload_to='competition_pictures')

    def __str__(self):
        return str(self.sport)

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.IntegerField(default=1)
    student_image = models.ImageField(default='std_default.jpg', upload_to='student_pictures')

    def __str__(self):
        return str(self.user.username)

class TeacherManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.TEACHER)

class Teacher(User):
    base_role = User.Role.TEACHER
    teacher = TeacherManager()
    class Meta:
        proxy = True

class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teacher_id = models.IntegerField(default=1)
    teacher_image = models.ImageField(default='teach_default.jpg', upload_to='teacher_pictures')


    def __str__(self):
        return str(self.user.username)

class Product(models.Model):
    added_by = models.ForeignKey(User, on_delete = models.CASCADE, default=User.base_role)
    prod_id = models.SmallIntegerField(default=0, null=False, unique=True)
    prod_name = models.CharField(max_length=30)
    prod_desc = models.CharField(max_length = 500, default='prod desc')
    prod_price = models.DecimalField(max_digits=10, decimal_places=2)
    prod_img = models.ImageField(default='prod-default.jpg',upload_to='product_pictures')

    def __str__(self):
        return str(self.prod_name)

class Order(models.Model):
    order_by = models.ForeignKey(User, on_delete = models.CASCADE)
    prod_ordered = models.ForeignKey(Product, on_delete = models.CASCADE,null=True)
    order_count = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.order_by)


    
    









    