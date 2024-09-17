from django.contrib import admin
# Register your models here.
from django.contrib.auth.models import User, Group
from django.db.models import ManyToOneRel

from analytics.apps.bot.models import BotUser, TelegramChat, TelegramSubscriber, InviteLink

admin.site.unregister(User)
admin.site.unregister(Group)

def get_fields_for_model(db_model) -> list[str]:
    fields = []
    for field in db_model._meta.get_fields():
        if isinstance(field, ManyToOneRel):
            continue
        fields.append(field.name)
    return fields

@admin.register(BotUser)
class BotUserAdmin(admin.ModelAdmin):
    list_display = get_fields_for_model(BotUser)
    search_fields = ['telegram_id', 'username', 'first_name', 'last_name']
    list_editable = ['first_name']
    list_filter = ['telegram_id', 'username', 'first_name', 'last_name']

@admin.register(TelegramChat)
class BotUserAdmin(admin.ModelAdmin):
    list_display = get_fields_for_model(TelegramChat)

@admin.register(TelegramSubscriber)
class BotUserAdmin(admin.ModelAdmin):
    list_display = get_fields_for_model(TelegramSubscriber)

@admin.register(InviteLink)
class BotUserAdmin(admin.ModelAdmin):
    list_display = get_fields_for_model(InviteLink)