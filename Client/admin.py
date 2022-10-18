from django.contrib import admin

from Client.models import ClientEvents, ClientPhone, Tag, Time

# Register your models here.


class ClientPhoneAdmin(admin.ModelAdmin):
    list_display = ["user", "phone"]


class ClientEventsAdmin(admin.ModelAdmin):
    list_display = ["user", "name", "date"]


admin.site.register(Tag)
admin.site.register(Time)
admin.site.register(ClientPhone, ClientPhoneAdmin)
admin.site.register(ClientEvents, ClientEventsAdmin)
