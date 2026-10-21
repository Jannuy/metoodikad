from django.urls import path

from .views import ApiRootView, FeedbackListCreateView, FeedbackSummaryView


urlpatterns = [
    path("", ApiRootView.as_view(), name="api-root"),
    path("feedback/", FeedbackListCreateView.as_view(), name="feedback-list-create"),
    path("summary/", FeedbackSummaryView.as_view(), name="feedback-summary"),
]
