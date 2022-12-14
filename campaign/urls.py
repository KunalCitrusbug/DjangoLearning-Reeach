from django.urls import include, path

from campaign.views import (
    AddActions,
    AddCampaignView,
    CampaignView,
    DeleteCampaign,
    UpdateCampaign,
    UpdateSettings,
)

app_name = "campaign"

urlpatterns = [
    path("", CampaignView.as_view(), name="campaign"),
    path("campaign-add/", AddCampaignView.as_view(), name="create_campaign"),
    path("campaign-edit/<int:pk>/", UpdateCampaign.as_view(), name="campaign_edit"),
    path("update-settings/<int:pk>/", UpdateSettings.as_view(), name="update_settings"),
    path("delete-campaign/<int:pk>/", DeleteCampaign.as_view(), name="delete_campaign"),
    path("add-actions/<int:pk>/", AddActions.as_view(), name="add_actions"),
]
