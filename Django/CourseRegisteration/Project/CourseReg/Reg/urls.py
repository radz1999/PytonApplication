from django.urls import path
from . import views
from django.contrib import admin

admin.autodiscover()


urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('course', views.course_list, name='course_list'),
    path('curriculum/<str:userNo>/',views.curriculum,name='curriculum'),
    path('course/<str:pk>/', views.course_detail, name='course_detail'),
    path('course/new', views.course_new, name='course_new'),
    path('course/<str:pk>/edit/', views.course_edit, name='course_edit'),
    path('register', views.register, name='register'),
    path('logout',views.logout_view,name='logout_view'),
    path('courseSelect/<str:userNo>/',views.courseSelect,name='courseSelect'),
    path('courseTaken/<str:userNo>/',views.course_taken,name='courseTaken'),

   ]
