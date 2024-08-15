from django.contrib import admin, messages
from .models import Women, Husband, Category


admin.site.register(Husband)


class MarriedFilter(admin.SimpleListFilter):
    title = "Статус женщин"
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('married', 'Замужем'),
            ('single', 'Не замужем'),
        ]
    
    def queryset(self, request, queryset):
        if self.value() == 'married':
            return queryset.filter(husband__isnull=False)
        elif self.value() == 'single':
            return queryset.filter(husband__isnull=True)


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    list_display = ("title", "time_create", "is_published", 'cat', 'brief_info',)
    list_display_links = ("title",)
    ordering = ["time_create", "title"]
    list_editable = ('is_published',)
    list_per_page = 5
    actions = ['set_published', 'set_unpublished']
    search_fields = ['title', 'cat__name']
    list_filter = [MarriedFilter, 'cat__name', 'is_published']

    @admin.display(description='Кол-во символов')
    def brief_info(self, women: Women):
        return f'{len(women.content)} символов'
    
    @admin.action(description='Опубликовать посты')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=1)
        self.message_user(request, f'Опубликовано {count} записей.')


    @admin.action(description='Убрать посты с публикации')
    def set_unpublished(self, request, queryset):
        count = queryset.update(is_published=0)
        self.message_user(request, f'Снято с публикации {count} записей.', messages.WARNING)


@admin.register(Category)
class WomenAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    ordering = ['id', 'name']
