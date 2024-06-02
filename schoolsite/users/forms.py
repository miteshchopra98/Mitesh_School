from dataclasses import fields
from django import forms
from django.forms import ModelForm
from schoolapp.models import *
from django.contrib.auth.forms import *
from users.models import *



class StudentRegisterForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'first_name','last_name','role','dob']



class TeacherRegisterForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'first_name','last_name','role','dob']


class AdminRegisterForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'first_name','last_name','role','dob']

class StudentMarksForm(ModelForm):
    class Meta:
        model = StudentMarks
        fields = ['English', 'Hindi','Marathi','Maths','Science','Total']
    
class StudentCompetitionForm(ModelForm):
    class Meta:
        model = StudentCompetition
        fields = ['comp', 'sport','sport_desc', 'sport_image']

class ProductCountForm(ModelForm):
    class Meta:
        model = Order
        fields = ['order_count']

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['added_by','prod_id', 'prod_name', 'prod_desc', 'prod_price', 'prod_img']
