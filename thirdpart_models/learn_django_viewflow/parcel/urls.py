from django.conf.urls import url, include
from viewflow.flow.viewset import FlowViewSet
from viewflow.flow.views import CreateProcessView, UpdateProcessView
from .flows import DeliveryFlow
from . import views


from django.urls import re_path

delivery_urls = FlowViewSet(DeliveryFlow).urls

urlpatterns = [
    re_path('^temp&', views.index, name='index'),
    # re_path('^start/',
    #     CreateProcessView.as_view(), {
    #         'flow_class': DeliveryFlow,
    #         'flow_task': DeliveryFlow.start
    #     },
    #     name='my-wkfl')
]
