from django.urls import path, include
from campaign.views import CampaignView, AddCampaignView

app_name = "campaign"

urlpatterns = [
    path("campaign/", CampaignView.as_view(), name="campaign"),
    path("add_Campaign/", AddCampaignView.as_view(), name="create_campaign"),
]
