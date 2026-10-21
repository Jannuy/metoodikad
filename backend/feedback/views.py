from django.db.models import Avg, Count
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Feedback
from .serializers import FeedbackSerializer


class ApiRootView(APIView):
    def get(self, request):
        return Response(
            {
                "feedback": reverse("feedback-list-create", request=request),
                "summary": reverse("feedback-summary", request=request),
            }
        )


class FeedbackListCreateView(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class FeedbackSummaryView(APIView):
    def get(self, request):
        summary = (
            Feedback.objects.values("subject")
            .annotate(
                count=Count("id"),
                average=Avg("rating"),
                clarity_average=Avg("clarity_rating"),
                participation_average=Avg("participation_rating"),
            )
            .order_by("subject")
        )
        data = [
            {
                "subject": row["subject"],
                "count": row["count"],
                "average": round(row["average"], 1),
                "clarity_average": (
                    round(row["clarity_average"], 1)
                    if row["clarity_average"] is not None
                    else None
                ),
                "participation_average": (
                    round(row["participation_average"], 1)
                    if row["participation_average"] is not None
                    else None
                ),
            }
            for row in summary
        ]
        return Response(data)
