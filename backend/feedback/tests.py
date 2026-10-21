from rest_framework.test import APITestCase

from .models import Feedback


class ApiRootTests(APITestCase):
    def test_api_root_lists_available_endpoints(self):
        response = self.client.get("/api/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data,
            {
                "feedback": "http://testserver/api/feedback/",
                "summary": "http://testserver/api/summary/",
            },
        )


class FeedbackSubmissionTests(APITestCase):
    def test_feedback_includes_clarity_and_participation_ratings(self):
        response = self.client.post(
            "/api/feedback/",
            {
                "name": "Test",
                "class_name": "10.B",
                "subject": "Matemaatika",
                "teacher": "Kadri Agu",
                "rating": 4,
                "clarity_rating": 3,
                "participation_rating": 5,
            },
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["clarity_rating"], 3)
        self.assertEqual(response.data["participation_rating"], 5)
        self.assertEqual(response.data["teacher"], "Kadri Agu")

    def test_feedback_rejects_out_of_range_question_ratings(self):
        response = self.client.post(
            "/api/feedback/",
            {
                "name": "Test",
                "class_name": "10.B",
                "subject": "Matemaatika",
                "teacher": "Kadri Agu",
                "rating": 4,
                "clarity_rating": 6,
                "participation_rating": 5,
            },
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn("clarity_rating", response.data)

    def test_feedback_requires_question_ratings(self):
        response = self.client.post(
            "/api/feedback/",
            {
                "name": "Test",
                "class_name": "10.B",
                "subject": "Matemaatika",
                "teacher": "Kadri Agu",
                "rating": 4,
            },
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn("clarity_rating", response.data)
        self.assertIn("participation_rating", response.data)
        self.assertIn("teacher", response.data)

    def test_summary_includes_question_rating_averages(self):
        Feedback.objects.create(
            name="Test",
            class_name="10.B",
            subject="Matemaatika",
            teacher="Kadri Agu",
            rating=4,
            clarity_rating=3,
            participation_rating=5,
        )

        response = self.client.get("/api/summary/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data,
            [
                {
                    "subject": "Matemaatika",
                    "count": 1,
                    "average": 4.0,
                    "clarity_average": 3.0,
                    "participation_average": 5.0,
                }
            ],
        )
