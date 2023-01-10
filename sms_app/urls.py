from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("Message", api.MessageViewSet)
router.register("Recipient", api.RecipientViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("sms_app/Message/", views.MessageListView.as_view(), name="sms_app_Message_list"),
    path("sms_app/Message/Dashboard/", views.MessageListGroupedView.as_view(), name="sms_app_Message_Dashboard"),
    path("sms_app/Message/create/", views.MessageCreateView.as_view(), name="sms_app_Message_create"),
    path("sms_app/Message/detail/<int:pk>/", views.MessageDetailView.as_view(), name="sms_app_Message_detail"),
    path("sms_app/Message/update/<int:pk>/", views.MessageUpdateView.as_view(), name="sms_app_Message_update"),
    path("sms_app/Message/delete/<int:pk>/", views.MessageDeleteView.as_view(), name="sms_app_Message_delete"),
    path("sms_app/Recipient/", views.RecipientListView.as_view(), name="sms_app_Recipient_list"),
    path("sms_app/Recipient/create/", views.RecipientCreateView.as_view(), name="sms_app_Recipient_create"),
    path("sms_app/Recipient/detail/<int:pk>/", views.RecipientDetailView.as_view(), name="sms_app_Recipient_detail"),
    path("sms_app/Recipient/update/<int:pk>/", views.RecipientUpdateView.as_view(), name="sms_app_Recipient_update"),
    path("sms_app/Recipient/delete/<int:pk>/", views.RecipientDeleteView.as_view(), name="sms_app_Recipient_delete"),
    path("sms_app/UploadSms/", views.UploadSmsListView.as_view(), name="sms_app_UploadSms_list"),
    path("sms_app/ValidateExcel/", views.import_data, name="sms_app_import_data"),
    path('sms_app/approve_sms/<str:link_code>/', views.approve_sms, name='approve_sms'),
    path('sms_app/reject_sms/<str:link_code>'/, views.reject_sms, name='reject_sms'),
    path('sms_app/Message/detail/<str:link_code>/', views.MessageDetailApprovedView.as_view(), name="sms_app_Message_approved_detail"),


)
