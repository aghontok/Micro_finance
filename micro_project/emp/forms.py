from .models import *
from django.forms import (ModelForm,Textarea,DateInput,TextInput,Select,
                          EmailInput,FileInput,ImageField,)



from django import forms
"""form form emp apps"""

class  EmpForm(ModelForm):
    class Meta:
        model=Emp
        fields='__all__'
        widgets={
            'emp_id':TextInput(attrs={'class':'form-control',}),
            'emp_bod':DateInput(attrs={'type':'date','class':'form-control',}),
            'emp_first_name':TextInput(attrs={'class':'form-control',}),
            'emp_last_name':TextInput(attrs={'class':'form-control',}),
            'emp_father_name':TextInput(attrs={'class':'form-control'}),
            'emp_mother_name':TextInput(attrs={'class':'form-control'}),
            'emp_married':Select(attrs={'class':'form-select'}),
            'emp_address':Textarea(attrs={'class':'form-control','cols':'10','rows':'4'}),
            'emp_gender':Select(attrs={'class':'form-control'}),
            'emp_phone':TextInput(attrs={'class':'form-control'}),
            'emp_email':EmailInput(attrs={'class':'form-control'}),
            'emp_salary':TextInput(attrs={'class':'form-control'}),
            'emp_blood':TextInput(attrs={'class':'form-control'}),
            'emp_manager':Select(attrs={'class':'form-select'}),
            'emp_job':Select(attrs={'class':'form-select'}),
            'emp_branch':Select(attrs={'class':'form-select'}),
            'emp_photo':FileInput(attrs={'class':'form-control'}),
                 }




class  LocationForm(ModelForm):
    class Meta:
        model=Locations
        fields = '__all__'


class BranchForm(ModelForm):

    class Meta:
        model=Branches
        fields='__all__'
        widgets={'bran_address':Textarea(attrs={'class':'class1'}),
                 'bran_name':TextInput(attrs={'class':'class1'}),
                 'bran_location':Select(attrs={'class':'class1'}),
                 }


class JobForm(ModelForm):
    class Meta:
        model=Jobs
        fields = '__all__'

