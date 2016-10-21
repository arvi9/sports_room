from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import StudentCreationForm
from django.views.generic import CreateView


@login_required(login_url='/login/')
def index(request):
    return render(request, 'index.html')


class CreateStudentView(CreateView):
    form_class = StudentCreationForm
    template_name = 'registration/registration_form.html'
    success_url = '/'

