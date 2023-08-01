from django.db import models

# Create your models here.
class Reklama(models.Model):
    class Meta:
        db_table = 'reklamka'

    title = models.CharField("заголовок", max_length=128)
    text = models.TextField("текст")
    price = models.FloatField("цена")
    user = models.CharField("пользователь", max_length=126)  # Просто имя
    date = models.DateField("дата", auto_now_add=True)
    def __str__(self):
        return f"{self.text}, {self.price}, {self.title}"

