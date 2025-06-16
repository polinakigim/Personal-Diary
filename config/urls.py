from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jotly/', include('diary.urls)', namespace='diary'))
]
