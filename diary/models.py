from django.db import models

from users.models import User


class Entry(models.Model):
    title = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Заголовок"
    )
    content = models.TextField(verbose_name="Содержимое")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = (
        models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения"),
    )
    owner = models.ForeignKey(
        User, verbose_name="Владелец", blank=True, null=True, on_delete=models.SET_NULL
    )

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.content[:50]} — {self.created_at}"
