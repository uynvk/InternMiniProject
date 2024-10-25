from django.urls import path
from hire_center.views.company import company_register

urlpatterns = [
    path("company/", company_register),
]
