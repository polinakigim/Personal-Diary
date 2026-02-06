from django.urls import path

from diary.apps import DiaryConfig
from diary.views import (EntryCreateView, EntryDeleteView, EntryDetailView,
                         EntryListView, EntryUpdateView, contacts, features,
                         home)

app_name = DiaryConfig.name

urlpatterns = [
    path("home/", home, name="home"),
    path("contacts/", contacts, name="contacts"),
    path("features/", features, name="features"),
    path("entry/create/", EntryCreateView.as_view(), name="entry_create"),
    path("entry_list/", EntryListView.as_view(), name="entry_list"),
    path("entry_detail/<int:pk>/", EntryDetailView.as_view(), name="entry_detail"),
    path("entry/update/<int:pk>/", EntryUpdateView.as_view(), name="entry_update"),
    path("entry/delete/<int:pk>/", EntryDeleteView.as_view(), name="entry_delete"),
]
