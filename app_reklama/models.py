from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
# Create your models here.
class Reklama(models.Model):
    class Meta:
        db_table = 'reklamka'

    title = models.CharField("заголовок", max_length=128)
    text = models.TextField("текст")
    price = models.FloatField("цена")
    user = models.CharField("пользователь", max_length=126)  # Просто имя
    date = models.DateField("дата", auto_now_add=True)
    auction = models.BooleanField("торг", help_text='Возможен торг или нет', default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    @admin.display(description="дата создания")
    def created_date(self):


        if self.created_at.date() == timezone.now().date():
            create_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style = "color:green; font-weight = bold;">Сегодня в {}</span>', create_time
            )
        return self.created_at.strftime('%d.%m.%Y at %H:%M:%S')

    @admin.display(description="дата обновления")
    def update_date(self):
        if self.update_at.date() == timezone.now().date():
            update_time = self.update_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style = "color:green; font-weight = bold;">Сегодня в {}</span>', update_time
            )
        return self.update_at.strftime('%d.%m.%Y at %H:%M:%S')

    def __str__(self):
        return f"Reklama(text = {self.text}, price = {self.price}, title = {self.title})"




