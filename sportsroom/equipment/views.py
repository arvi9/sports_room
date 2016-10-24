from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models

from .forms import StudentCreationForm


class IndexView(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    context_object_name = 'all_equipments'
    login_url = '/login/'
    model = models.Equipment

    def post(self, request, *args, **kwargs):
        equipment_id = request.POST.get('equipment')
        equipment = models.Equipment.objects.get(id=equipment_id)
        student = models.Student.objects.get(user__username=request.user)
        entry = models.Queue(student=student, equipment=equipment)
        entry.save()
        print(">>Q entry made")
        return super(IndexView, self).get(self, request, args, kwargs)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        user_fine = models.Student.objects.get(user__username=self.request.user).fine
        extra_context = {'user_fine': user_fine}
        context.update(extra_context)
        return context


class CreateStudentView(CreateView):
    form_class = StudentCreationForm
    template_name = 'registration/registration_form.html'
    success_url = '/'

# def student_login(request, **kwargs):
#    print(request.user)
#    print("hello")
#    if request.user.is_authenticated:
#        return render(request, 'index.html')
#    else:
#        login(request, **kwargs)
