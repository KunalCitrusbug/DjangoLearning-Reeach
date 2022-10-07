from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views import View
import datetime

from Client.models import ClientEvents, Tag, ClientPhone, Time
from campaign.models import Campaign, Trigger


# Create your views here.
class CampaignView(View):
    template_name = "client/campaigns.html"

    def get(self, *args, **kwargs):
        context = {'campaign_data': Campaign.objects.filter(user=self.request.user)}
        return render(self.request, self.template_name, context=context)


class AddCampaignView(View):
    template_name = "client/create_campaign.html"

    def get(self, *args, **kwargs):
        current_time = datetime.datetime.now().time()
        current_date = datetime.date.today()
        client_date = ClientEvents.objects.filter(user=self.request.user)
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
            phone = get_object_or_404(ClientPhone, phone=self.request.POST.get("phone"))
            id = Campaign.objects.create(user=self.request.user,
                                         name=name,
                                         steps=0,
                                         in_progress=0,
                                         complete=0,
                                         status="True",
                                         send_number=phone,
                                         sending_window="True",
                                         sent_days=("Mon", "Tues", "Wens", "Thurs", "Fri", "Sat"),
                                         start_time=datetime.time(8, 0, 0),
                                         end_time=datetime.time(20, 0, 0),
                                         ).id
            campaign_name = Campaign.objects.get(name=name)
            Trigger.objects.create(
                campaign=campaign_name,
                type=self.request.POST.get("type"),
                phone=phone,
                keyword=keyword_data
            )
            return JsonResponse({'status': 'success', 'pk': id})

        elif self.request.POST.get("type") == "date_based_trigger":
            id = Campaign.objects.create(user=self.request.user,
                                         name=name,
                                         steps=0,
                                         in_progress=0,
                                         complete=0,
                                         status="True",
                                         sending_window="True",
                                         sent_days=("Mon", "Tues", "Wens", "Thurs", "Fri", "Sat"),
                                         start_time=datetime.time(8, 0, 0),
                                         end_time=datetime.time(20, 0, 0),
                                         ).id
            campaign = Campaign.objects.get(pk=id)
            date = self.request.POST.get("date")
            Trigger.objects.create(
                campaign=campaign,
                type=self.request.POST.get("type"),
                select_date=ClientEvents.objects.get(user=self.request.user, name=date),
                select_before_date=self.request.POST.get("day")
            )
            return JsonResponse({'status': 'success', "pk": id})

        elif self.request.POST.get("type") == "tag_based_trigger":
            id = Campaign.objects.create(user=self.request.user,
                                         name=name,
                                         steps=0,
                                         in_progress=0,
                                         complete=0,
                                         status="True",
                                         sending_window="True",
                                         sent_days=("Mon", "Tues", "Wens", "Thurs", "Fri", "Sat"),
                                         start_time=datetime.time(8, 0, 0),
                                         end_time=datetime.time(20, 0, 0),
                                         ).id
            campaign = Campaign.objects.get(pk=id)
            Trigger.objects.create(
                campaign=campaign,
                type=self.request.POST.get("type"),
                select_tags=self.request.POST.get("tags"),
            )
            return JsonResponse({'status': 'success', "pk": id})


class UpdateCampaign(View):
    model = Campaign
    template_name = "client/campaigns_edit.html"

    def get(self, *args, **kwargs):
        campaign_obj = get_object_or_404(Campaign, id=kwargs.get('pk'))
        trigger_obj = get_object_or_404(Trigger, campaign=campaign_obj)
        context = {"campaign_obj": campaign_obj, 'trigger_obj': trigger_obj,
                   "client_phone": ClientPhone.objects.filter(user=self.request.user), "time_obj": Time.objects.all()}
        return render(self.request, self.template_name, context)


class DeleteCampaign(View):
    def get(self, *args, **kwargs):
        campaign_obj = get_object_or_404(Campaign, id=kwargs.get('pk'))
        Campaign.objects.get(id=campaign_obj).delete()
        return JsonResponse({'status': 'success'})
