from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone
from django.views import View
import datetime

from Client.models import ClientEvents, Tag, ClientPhone
from campaign.models import Campaign, Trigger


# Create your views here.
class CampaignView(View):
    template_name = "client/campaigns.html"

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name)


class AddCampaignView(View):
    template_name = "client/create_campaign.html"

    def get(self, *args, **kwargs):
        current_time = datetime.datetime.now().time()
        current_date = datetime.date.today()
        client_date = ClientEvents.objects.filter(user=self.request.user)
        ClientPhone.objects.filter(user=self.request.user)
        tags = Tag.objects.all()
        context = {'time': current_time,
                   'date': current_date,
                   'date_obj': client_date,
                   'tags': tags,
                   'client_phone': ClientPhone.objects.filter(user=self.request.user)}
        return render(self.request, self.template_name, context=context)

    def post(self, *args, **kwargs):
        name = self.request.POST.get("name")
        if self.request.POST.get("type") == "keyword_based_trigger":
            keyword_data = self.request.POST.get("keyword")
            phone = self.request.POST.get("phone")
            Campaign.objects.create(user=self.request.user,
                                    name=name,
                                    steps=0,
                                    in_progress=0,
                                    complete=0,
                                    status="True")
            campaign_name = Campaign.objects.get(name=name)
            Trigger.objects.create(
                campaign=campaign_name,
                type=self.request.POST.get("type"),
                phone=phone,
                keyword=keyword_data
            )
            return JsonResponse({'status': 'success'})

        elif self.request.POST.get("type") == "date_based_trigger":
            id = Campaign.objects.create(user=self.request.user,
                                         name=name,
                                         steps=0,
                                         in_progress=0,
                                         complete=0,
                                         status="True").id
            campaign = Campaign.objects.get(pk=id)
            date = self.request.POST.get("date")
            Trigger.objects.create(
                campaign=campaign,
                type=self.request.POST.get("type"),
                select_date=ClientEvents.objects.get(user=self.request.user, name=date).date,
                select_before_date=self.request.POST.get("day")
            )
            return JsonResponse({'status': 'success'})

        elif self.request.POST.get("type") == "tag_based_trigger":
            id = Campaign.objects.create(user=self.request.user,
                                         name=name,
                                         steps=0,
                                         in_progress=0,
                                         complete=0,
                                         status="True").id
            campaign = Campaign.objects.get(pk=id)
            Trigger.objects.create(
                campaign=campaign,
                type=self.request.POST.get("type"),
                select_tags=self.request.POST.get("tags"),
            )
            return JsonResponse({'status': 'success'})
