from django.db.models import Avg, Count
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Feedback
from .serializers import FeedbackSerializer


class FeedbackListCreateView(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class FeedbackSummaryView(APIView):
    def get(self, request):
        summary = (
            Feedback.objects.values("subject")
            .annotate(count=Count("id"), average=Avg("rating"))
            .order_by("subject")
        )
        data = [
            {
                "subject": row["subject"],
                "count": row["count"],
                "average": round(row["average"], 1),
            }
            for row in summary
        ]
        return Response(data)
