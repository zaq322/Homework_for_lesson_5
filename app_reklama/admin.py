from django.contrib import admin
from .models import Reklama

# Register your models here.
class ReklamaAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'price', 'user', 'date', 'auction', 'created_at','update_at','created_date','update_date']
    list_filter = ['auction','created_at']
    actions = ['make_auction_as_false', 'make_auction_as_true'] #указываем функции
    fieldsets = (
        (
            'Общее', #Добавляем красивый блок "общее"
            {
                "fields":('title', 'text')
            }
         ),
        (
            'Финансы', #Добавили красивый блок "Финансы"
            {
                "fields":('price', 'auction'),
                "classes":['collapse'] #Для скрытия
            }
        )
    )


    @admin.action(description='Добавить возможность торга')#создаём функции
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction = True)

    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction = False)
















#Указал модель и админ класс(для кастомизации)
admin.site.register(Reklama, ReklamaAdmin)
