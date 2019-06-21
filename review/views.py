from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.http import JsonResponse


from .serializers import ReviewListSerializer
from .models import Review
from booking.models import Booking
from property.models import Proparty


class CreatePropartyReviewByUserApiView(APIView):
    permission_classes = [AllowAny]

    # host, user, proparty_id, text, score
    def post(self, request):
        user = self.request.GET.get("user")
        host = self.request.GET.get("host")

        proparty = self.request.GET.get("proparty_id")
        text = self.request.GET.get("text")
        score = self.request.GET.get("score")
        if user.is_authenticated or True:
            proparty = Proparty.objects.filter(proparty=proparty)
            if proparty.exists():
                booking = Booking.objects.filter(user=user, host=host)  # also check trip ended or not
                if booking.exists():
                    review_instance = Review.objects.create(
                        review_on=host,
                        review_by=user,
                        proparty=proparty,
                        created_by=1,
                        review=text,
                        score=score
                    )
                    return JsonResponse({"created": True})
                else:
                    return JsonResponse({"created": False})
            else:
                return JsonResponse({"created": False})
        return JsonResponse({"created": False})


class CreateUserReviewByHostApiView(APIView):
    permission_classes = [AllowAny]

    # host, user, text, score
    def post(self, request):
        user = self.request.GET.get("user")
        host = self.request.GET.get("host")

        proparty = self.request.GET.get("proparty_id")
        text = self.request.GET.get("text")
        score = self.request.GET.get("score")
        if user.is_authenticated or True:
            proparty = Proparty.objects.filter(proparty=proparty)
            if proparty.exists():
                booking = Booking.objects.filter(user=user, host=host)  # also check trip ended or not
                if booking.exists():
                    review_instance = Review.objects.create(
                        review_on=user,
                        review_by=host,
                        created_by=0,
                        review=text,
                        score=score
                    )
                    return JsonResponse({"created": True})
                else:
                    return JsonResponse({"created": False})
            else:
                return JsonResponse({"created": False})
        return JsonResponse({"created": False})


class PropartyReviewListApiView(APIView):
    permission_classes = [AllowAny]

    # proparty_id
    def get(self, request):
        data = []
        property_id = self.request.GET.get("property_id")
        property_review_list = Review.objects.filter(proparty=property_id)
        for review in property_review_list:
                temp = {}
                temp['user'] = review.reviewed_by
                temp['text'] = review.text
                temp['score'] = review.score
                temp['created_at'] = review.created_at
                temp['comments'] = []

                comment_list = Comment.objects.filter(review=reviews.id)
                for comment in comment_list:
                    temp_comment = {}
                    temp_comment['user'] = comment.user
                    temp_comment['text'] = comment.text
                    temp_comment['created_at'] = comment.created_at
                    temp['comments'].append(temp_comment)
                data.append(temp)

        return JsonResponse({"data": data})


class UserReviewListApiView(APIView):
    permission_classes = [AllowAny]

    # user
    def get(self, request):
        data = []
        user = self.request.GET.get("user")
        user_review_list = Review.objects.filter(reviewed_on=user)
        for review in user_review_list:
                temp = {}
                temp['user'] = review.reviewed_by
                temp['text'] = review.text
                temp['score'] = review.score
                temp['created_at'] = review.created_at
                temp['comments'] = []

                comment_list = Comment.objects.filter(review=reviews.id)
                for comment in comment_list:
                    temp_comment = {}
                    temp_comment['user'] = comment.user
                    temp_comment['text'] = comment.text
                    temp_comment['created_at'] = comment.created_at
                    temp['comments'].append(temp_comment)
                data.append(temp)

        return JsonResponse({"data": data})
