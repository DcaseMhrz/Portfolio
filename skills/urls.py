from django.urls import path
from skills import views

urlpatterns = [
    path('',views.showskills,)
]
