from django.views import generic
from django.shortcuts import render, redirect

from viewflow.decorators import flow_start_view, flow_view
from viewflow.flow.views import StartFlowMixin, FlowMixin
from viewflow.flow.views.utils import get_next_task_url

from . import models


from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")



# class FirstBoodSampleView(StartFlowMixin):
#     template_name = 'bloodtest/bloodtest/first_sample.html'

#     form_list = [forms.PatientForm, forms.BloodSampleForm]

#     def done(self, form_list, form_dict, **kwargs):
#         patient = form_dict['0'].save()

#         sample = form_dict['1'].save(commit=False)
#         sample.patient = patient
#         sample.taken_by = self.request.user
#         sample.save()

#         self.activation.process.sample = sample
#         self.activation.done()

#         return redirect(
#             get_next_task_url(self.request, self.activation.process))
