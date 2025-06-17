from django.urls import path
from diary.apps import DiaryConfig
from diary.views import home, dashboard, features, contacts

app_name = DiaryConfig.name

urlpatterns = [
    path('home/', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('contacts/', contacts, name='contacts'),
    path('features/', features, name='features'),
]
