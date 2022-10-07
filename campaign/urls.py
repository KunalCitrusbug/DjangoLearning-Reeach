from django.urls import path, include
from campaign.views import CampaignView, AddCampaignView, UpdateCampaign

app_name = "campaign"

urlpatterns = [
    path("", CampaignView.as_view(), name="campaign"),
    path("campaign-add/", AddCampaignView.as_view(), name="create_campaign"),
    path("campaign-edit/<int:pk>/", UpdateCampaign.as_view(), name="campaign_edit"),
    path("campaiogn-delete/<int:pk>/", DeleteCampaign.as_view(),name="campaign_delete")
]
