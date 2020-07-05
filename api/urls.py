from django.urls import path

from api import views

urlpatterns=[
    path("user/",views.UserAPIView.as_view()),
    path("emp/",views.EmployeeView.as_view()),
    path("emp/<str:id>",views.EmployeeView.as_view()),
]