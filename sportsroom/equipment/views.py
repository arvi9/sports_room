




from django.shortcuts import render
from django.views import generic
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from . import models

from .forms import StudentCreationForm


#@login_required(login_url='/login/')
#def index(request):
#    return render(request, 'index.html')


@login_required(login_url='/login/')
class IndexView(generic.ListView):
    template_name = 'templates/index.html'
    context_object_name = 'all_equipments'
    def get_queryset(self):
        return models.Equipment.objects.all()


class CreateStudentView(CreateView):
    form_class = StudentCreationForm
    template_name = 'registration/registration_form.html'
    success_url = '/'

