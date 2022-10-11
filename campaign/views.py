from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views import View
import datetime

from Client.models import ClientEvents, Tag, ClientPhone, Time
from campaign.models import Campaign, Trigger, Action


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
                                         start_time=Time.objects.get(name="8 A.M"),
                                         end_time=Time.objects.get(name="8 P.M"),
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
                                         start_time=Time.objects.get(name="8 A.M"),
                                         end_time=Time.objects.get(name="8 P.M"),
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
                                         start_time=Time.objects.get(name="8 A.M"),
                                         end_time=Time.objects.get(name="8 P.M"),
                                         ).id
            campaign = Campaign.objects.get(pk=id)
            Trigger.objects.create(
                campaign=campaign,
                type=self.request.POST.get("type"),
                select_tags=Tag.objects.get(name=self.request.POST.get("tag")),
            )
            return JsonResponse({'status': 'success', "pk": id})


class UpdateCampaign(View):
    model = Campaign
    template_name = "client/campaigns_edit.html"

    def get(self, *args, **kwargs):
        campaign_obj = get_object_or_404(Campaign, id=kwargs.get('pk'))
        min_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                    27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51,
                    2, 53, 54, 55, 56, 57, 58, 59]
        trigger_obj = get_object_or_404(Trigger, campaign=campaign_obj)
        context = {"campaign_obj": campaign_obj, 'trigger_obj': trigger_obj,
                   "client_phone": ClientPhone.objects.filter(user=self.request.user),
                   "time_obj": Time.objects.all(),
                   "min_list": min_list,
                   "tags": Tag.objects.all()}
        return render(self.request, self.template_name, context)


class DeleteCampaign(View):
    def post(self, *args, **kwargs):
        campaign_obj = get_object_or_404(Campaign, id=kwargs.get('pk')).delete()
        return JsonResponse({'status': 'success'})


class UpdateSettings(View):
    def post(self, *args, **kwargs):

        campaign_obj = get_object_or_404(Campaign, id=kwargs.get('pk'))
        campaign_obj.sending_window = self.request.POST.get("send_checkbox")
        if self.request.POST.get("monday") == "True":
            monday = "Mon"
        else:
            monday = "False"

        if self.request.POST.get("tuesday") == "True":
            tuesday = "Tues"
        else:
            tuesday = "False"

        if self.request.POST.get("wednesday") == "True":
            wednesday = "Wens"
        else:
            wednesday = "False"

        if self.request.POST.get("thursday") == "True":
            thursday = "Thurs"
        else:
            thursday = "False"

        if self.request.POST.get("friday") == "True":
            friday = "Fri"
        else:
            friday = "False"

        if self.request.POST.get("saturday") == "True":
            saturday = "Sat"
        else:
            saturday = "False"

        if self.request.POST.get("sunday") == "True":
            sunday = "Sun"
        else:
            sunday = "False"

        campaign_obj.sent_days = (monday, tuesday, wednesday, thursday, friday, saturday, sunday)
        campaign_obj.start_time = Time.objects.get(name=self.request.POST.get("start_time"))
        campaign_obj.end_time = Time.objects.get(name=self.request.POST.get("end_time"))
        campaign_obj.send_number = ClientPhone.objects.get(phone=self.request.POST.get("send_number"))
        campaign_obj.double_optin = self.request.POST.get("double_optin_checkbox")
        campaign_obj.double_optin_keyword = self.request.POST.get("double_optin_keyword")
        campaign_obj.double_optin_message = self.request.POST.get("Double_optin_message")
        campaign_obj.limit_multiple = self.request.POST.get("Limit_multiple_checkbox")
        campaign_obj.limit_multiple_message = self.request.POST.get("Limit_multiple_message")
        campaign_obj.cancellation_trigger = self.request.POST.get("Cancellation_trigger_checkbox")
        campaign_obj.on_reply = self.request.POST.get("on_reply")
        campaign_obj.save()

        return JsonResponse({'status': 'success', "pk": kwargs.get('pk')})


class AddActions(View):
    def post(self, *args, **kwargs):

        campaign_obj = get_object_or_404(Campaign, id=kwargs.get('pk'))
        Action.objects.create(
            campaign=campaign_obj,
            text_message=self.request.POST.get("text_message"),
            number=self.request.POST.get("time_delay_no"),
            duration=self.request.POST.get("duration"),
            wait_until=(self.request.POST.get("wait_hour"), self.request.POST.get("wait_minute"), 00),
            tag=Tag.objects.get(name=self.request.POST.get("tag")),
        )

        return JsonResponse({'status': 'success'})
