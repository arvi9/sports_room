from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.CreateStudentView.as_view(), name='register'),
    url(r'^', include('django.contrib.auth.urls')),
]
