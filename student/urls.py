from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('contact/<str:name>',views.contact),
    path('emp/',views.emp,name='emp'),

    # student crud
    path('student/add/',views.stud_add,name='add'),
    path('student/list/',views.stud_list, name='list'),
]
