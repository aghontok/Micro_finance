"""
Url configure for emp apps
"""

from django.urls import path
from . import views

urlpatterns = [

    path('loc_list',views.LocationList,name='list_loc'),
    path('loc_edit/<id>/', views.LocationUpdate, name='edit_loc'),
    path('loc_del/<id>/', views.LocationDel, name='del_loc'),
    path('loc_add', views.LocationAdd, name='add_loc'),
    path('bran_list', views.BranchList, name='list_bran'),
    path('bran_edit/<id>/', views.BranchUpdate, name='edit_bran'),
    path('bran_del/<id>/', views.BranchDel, name='del_bran'),
    path('bran_add/', views.BranchAdd, name='add_bran'),
    # path('bran_add',views.BranAdd,name='add_br'),
    # path('bran_add_save',views.BranAdd_Save,name='add_br_save'),
    path('list/', views.EmpList, name='list_emp'),
    path('details/<id>', views.EmpDetails, name='details_emp'),
    path('edit/<id>', views.EmpUpdate, name='edit_emp'),
    path('del/<id>', views.EmpDel, name='del_emp'),
    path('crt', views.EmpAdd, name='crt_emp'),
    path('job/', views.JobList, name='list_job'),
]
