from django.urls import path
from hire_center.views.candidate import candidate_detail, candidate_list

urlpatterns = [
    path("candidates/", candidate_list),
    path("candidates/<int:pk>/", candidate_detail),
]
