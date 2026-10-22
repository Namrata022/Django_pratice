from django.urls import path
from . import views
from .views import(
    CourseCreateView,
    CourseDeleteView,
    CourseDetailView,
    CourseListView,
    CourseUpdateView
)

urlpatterns=[
    path('',views.home,name='home'),
    path('contact/<str:name>',views.contact),
    path('emp/',views.emp,name='emp'),

    # student crud
    path('student/add/',views.stud_add,name='add'),
    path('student/list/',views.stud_list, name='list'),
    path('student/edit/<int:id>/',views.stud_edit, name='edit'),
    path('student/delete/<int:id>/',views.stud_delete, name='delete'),

    # employee crud
    path('employee/add',views.emp_add,name='Eadd'),
    path('employee/list',views.emp_list,name='Elist'),
    path('employee/edit/<int:id>/',views.emp_edit,name='Eedit'),
    path('employee/delete/<int:id>/',views.emp_delete, name='Edelete'),

    # session
    path('create/',views.create_session,name='create'),
    path('show/',views.show_session,name='show_session'),
    path('modify/',views.modify_session,name='modify'),
    path('delete/',views.delete_session,name='delete'),

    # Auth
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),

    # CBV course crud
    path('course_list',CourseListView.as_view(),name='course_list'),
    path('course_add/',CourseCreateView.as_view(),name='course_add'), 
    path('course/<int:pk>/',CourseDetailView.as_view(),name='course_detail'), 
    path('course/<int:pk>/edit/',CourseUpdateView.as_view(),name='course_edit'), 
    path('course/<int:pk>/delete/',CourseDeleteView.as_view(),name='course_delete'), 

    # AJax 
    path('email_check/',views.email_check_page,name='email_check_page'),
    path('check_email/',views.check_email,name='check_email')
]
