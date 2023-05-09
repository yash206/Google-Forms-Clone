from django.urls import path
from . import views

app_name = 'Forms'

urlpatterns = [
    path('', views.home,name = 'home'),
    path('create/', views.create, name='create'),
    path('forms/<str:pk>/edit', views.update_form, name='update_form'),
    path('response/<str:pk>/viewForm', views.get_response_from_user, name='view_form'),
    path('forms/<str:pk>/responses', views.responses, name='responses'),
]