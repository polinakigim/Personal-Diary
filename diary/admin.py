from django.contrib import admin

from diary.models import Entry


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "content", "owner")
    list_filter = ("title",)
    search_fields = (
        "owner",
        "title",
    )
