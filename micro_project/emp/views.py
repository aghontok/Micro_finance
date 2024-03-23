from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required,permission_required
from .models import *
from .forms import *
# Create your views here.

def LocationList(request):
    l=Locations.objects.all()
    return render(request,'locations/loc_list.html',{'loc':l})


def LocationAdd(request):
    if request.method=='POST':
        form=LocationForm(request.POST)
        if form.is_valid():
            form.clean()
            form.save()
            c=form.cleaned_data['loc_city']
            d=form.cleaned_data['loc_district']
            v=form.cleaned_data['loc_division']
            context={'city':c,'district':d,'division':v}

            messages.success(request,'New location has been added')
            return render(request,'locations/loc_add_con.html',context)
        else:
            messages.error(request,'There has been error')
    else:
        form=LocationForm()
    return render(request,'locations/loc_add.html',{'form':form})




def  LocationUpdate(request,id):
    l=Locations.objects.get(loc_id=id)
    if request.method=='POST':
        form=LocationForm(request.POST,instance=l)
        if form.is_valid():
            form.clean()
            form.save()
            c=form.cleaned_data['loc_city']
            d=form.cleaned_data['loc_district']
            v=form.cleaned_data['loc_division']
            context={'city':c,'district':d,'division':v}
            messages.success(request,'Location has been updated')

            return render(request,'locations/loc_edit_con.html',context)
        else:
            messages.error(request,'There has been error')
    else:
        form=LocationForm(instance=l)
    return render(request,'locations/loc_edit.html',{'form':form})


def LocationDel(request,id):
    l=Locations.objects.get(loc_id=id)
    if l.loc_id==None:
        messages.warning(request,'Unable to delete')
    else:
        l.delete()
        messages.success(request,'Location is Deleted')
    return render(request,'locations/loc_del.html',{'loc':l})



def BranchList(request):
    b=Branches.objects.all()
    return render(request,'branches/bran_list.html',{'bran':b})

def BranchAdd(request):
    if request.method=='POST':
        form=BranchForm(request.POST)
        if form.is_valid():
            form.clean()
            form.save()
            n = form.cleaned_data['bran_name']
            a = form.cleaned_data['bran_address']
            l = form.cleaned_data['bran_location']
            context = {'name':n , 'address': a, 'location': l}
            messages.success(request,'New branches has been added')
            return render(request,'branches/bran_add_con.html',context)
        else:
            messages.error(request,'There has been error')
    else:
        form=BranchForm()

    return render(request,'branches/bran_add.html',{'form':form})


def BranAdd(request):
    l=Locations.objects.all()
    return render(request,'branches/br_add.html',{'loc':l})

def BranAdd_Save(request):
    form=BranchForm()
    if request.method!='POST':
        messages.error(request,'invalid method')
        return redirect('add_br')
    else:
        n=request.POST.get('name')
        a=request.POST.get('address')
        l=Locations.objects.get(loc_id=request.POST.get('location'))
        d=Branches(bran_name=n,
                   bran_address=a,bran_location=l)
        d.save()
        messages.success(request,'New Branch has been added')

        return redirect('add_br')









def  BranchUpdate(request,id):
    b=Branches.objects.get(bran_id=id)
    if request.method=='POST':
        form=BranchForm(request.POST,instance=b)
        if form.is_valid():
            form.clean()
            form.save()
            n = form.cleaned_data['bran_name']
            a = form.cleaned_data['bran_address']
            l = form.cleaned_data['bran_location']
            context = {'name':n, 'address': a, 'location': l}
            messages.success(request,'branch data has been updated')
            return render(request,'branches/bran_edit_con.html',context)
        else:
            messages.error(request,'There has been error')
    else:
        form=BranchForm(instance=b)
    return render(request,'branches/bran_edit.html',{'form':form})


def BranchDel(request,id):
    b=Branches.objects.get(bran_id=id)
    if b.bran_id== None:
        messages.warning(request,'Unable to delete')
    else:
        b.delete()
        messages.success(request,'The branch data has been deleted')
    return render(request,'branches/bran_del.html',{'bran':b})




def  EmpList(request):
    e=Emp.objects.all()
    return render(request,'emp/list_emp.html',{'emp':e})


def EmpDetails(request,id):
    e=get_object_or_404(Emp,pk=id)
    return render(request,'emp/emp_details_3.html',{'emp':e})


def EmpAdd(request):
    if request.method=='POST':
        form=EmpForm(request.POST)
        if  form.is_valid():
            form.save()
            messages.success(request,'New Employee has been added')
        else:
            messages.error(request,'There has been error')
    else:
        form=EmpForm()

    return render(request,'emp/emp_crt.html',{'form':form})

def EmpUpdate(request,id):
    e=Emp.objects.get(emp_id=id)
    if request.method=='POST':
        form=EmpForm(request.POST,request.FILES,instance=e)

        if form.is_valid():

            first_name=request.POST.get('emp_first_name')
            last_name=request.POST.get('emp_last_name')
            father_name=request.POST.get('emp_father_name')
            mother_name=request.POST.get('emp_mother_name')
            mar = request.POST.get('emp_married')
            add=request.POST.get('emp_address')
            phone=request.POST.get('emp_phone')
            email=request.POST.get('emp_email')
            gender=request.POST.get('emp_gender')
            bod=request.POST.get('emp_bod')
            salary=request.POST.get('emp_salary')
            blood=request.POST.get('emp_blood')
            m=request.POST.get('emp_manager')
            j=request.POST.get('emp_job')
            b=request.POST.get('emp_branch')
            photo=request.FILES.get('image')

            emp=Emp.objects.get(emp_manager=m)

            e.emp_first_name=first_name
            e.emp_last_name=last_name
            e.emp_father_name=father_name
            e.emp_mother_name=mother_name
            e.emp_married=mar
            e.emp_address=add
            e.emp_phone=phone
            e.emp_email=email
            e.emp_gender=gender
            e.emp_bod=bod
            e.emp_salary=salary
            e.emp_blood=blood
            e.emp_manager=emp.emp_manager
            e.emp_job=emp.emp_job
            e.emp_branch=emp.emp_branch
            e.emp_photo=photo

            e.save()
            messages.success(request,'Employee Information is updated')
        else:
            messages.error(request,'There has some error')

    else:
        form=EmpForm(instance=e)

    return render(request,'emp/emp_edit.html',{'form':form})

def EmpDel(request,id):
    e=Emp.objects.get(emp_id=id)
    if e.emp_id==None:
        messages.warning(request,'unable to delete')
    else:
        e.delete()
        messages.success(request,'Employee information has been deleted')
        return redirect('list_emp')


def JobList(request):
    j=Jobs.objects.all()
    return render(request,'emp/job_list.html',{'job':j})