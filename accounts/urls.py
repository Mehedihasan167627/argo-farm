from django.urls import path 

from .views import *

app_name="accounts"

urlpatterns=[
    path("login/",LoginView.as_view(),name="login"),
    path("register/",RegisterView.as_view(),name="register"),
    path("openingbalance/",OpeningbalanceView.as_view(),name="openingbalance"),
    path("financialyear/",FinancialYearView.as_view(),name="financialyear"),
]