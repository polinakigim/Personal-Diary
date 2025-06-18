from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from diary.forms import EntryForm
from diary.models import Entry


def home(request):
    return render(request, "home.html")


def features(request):
    return render(request, "features.html")


def contacts(request):
    return render(request, "contacts.html")


class EntryListView(LoginRequiredMixin, ListView):
    model = Entry

    def get_queryset(self):
        queryset = Entry.objects.filter(owner=self.request.user).order_by("-created_at")
        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_query"] = self.request.GET.get("q", "")
        return context


class EntryDetailView(LoginRequiredMixin, DetailView):
    model = Entry


class EntryCreateView(LoginRequiredMixin, CreateView):
    model = Entry
    form_class = EntryForm
    success_url = reverse_lazy("diary:entry_list")

    def form_valid(self, form):
        recipient = form.save()
        user = self.request.user
        recipient.owner = user
        recipient.save()
        return super().form_valid(form)


class EntryUpdateView(LoginRequiredMixin, UpdateView):
    model = Entry
    form_class = EntryForm
    success_url = reverse_lazy("diary:entry_list")


class EntryDeleteView(LoginRequiredMixin, DeleteView):
    model = Entry
    success_url = reverse_lazy("diary:entry_list")
