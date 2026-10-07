from django.urls import path

from .views import FeedbackListCreateView, FeedbackSummaryView


urlpatterns = [
    path("feedback/", FeedbackListCreateView.as_view(), name="feedback-list-create"),
    path("summary/", FeedbackSummaryView.as_view(), name="feedback-summary"),
]
