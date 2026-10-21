from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('contact/<str:name>',views.contact),
    path('emp/',views.emp,name='emp'),

    # student crud
    path('student/add/',views.stud_add,name='add'),
    path('student/list/',views.stud_list, name='list'),
    path('student/edit/<int:id>/',views.stud_edit, name='edit'),
    path('student/delete/<int:id>/',views.stud_delete, name='delete'),

    # session
    path('create/',views.create_session,name='create'),
    path('show/',views.show_session,name='show_session'),
    path('modify/',views.modify_session,name='modify'),
    path('delete/',views.delete_session,name='delete')
]
