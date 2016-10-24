from django.conf.urls import url, include
from django.contrib.auth.views import login
from . import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^register$', views.CreateStudentView.as_view(), name='register'),
    #url(r'^login$', views.student_login, name='login'),
    url(r'^', include('django.contrib.auth.urls')),
]
