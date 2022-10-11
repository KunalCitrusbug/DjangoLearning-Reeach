from django.contrib import admin

from campaign.models import Campaign, Trigger, Action


# Register your models here.
class CampaignAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'name',
        'date_created',
        'steps',
        'in_progress',
        'complete',
        'status',
    ]


class TriggerAdmin(admin.ModelAdmin):
    list_display = [
        "campaign",
        "type",
    ]


admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Action)
admin.site.register(Trigger, TriggerAdmin)
