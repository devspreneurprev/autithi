from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.http import JsonResponse


from .serializers import ReviewListSerializer
from .models import Review
from booking.models import Booking
from property.models import Proparty
from accounts.models import User
from review.models import Comment


class CreatePropartyReviewByUserApiView(APIView):
    permission_classes = [AllowAny]

    # host, user, proparty_id, text, score
    def post(self, request):
        user = self.request.GET.get("user")
        host = self.request.GET.get("host")

        proparty_id = self.request.GET.get("proparty_id")
        text = self.request.GET.get("text")
        score = self.request.GET.get("score")

        if True:  # user.is_authenticated
            print("start\n")
            proparty = Proparty.objects.get(id=proparty_id)
            print("read proparty fully\n")
            if proparty is not None:
                booking = Booking.objects.filter(user=user, host=host)  # also check trip ended or not
                print("read booking fully\n")
                if booking.exists():
                    print("booking exists")
                    user = User.objects.get(id=user)
                    host = User.objects.get(id=host)
                    review_instance = Review.objects.create(
                        reviewed_on=host,
                        reviewed_by=user,
                        proparty=proparty,
                        created_by=1,
                        text=text,
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

        text = self.request.GET.get("text")
        score = self.request.GET.get("score")

        if True:  # user.is_authenticated
            booking = Booking.objects.filter(user=user, host=host)  # also check trip ended or not
            print("read booking fully\n")
            if booking.exists():
                print("booking exists")
                user = User.objects.get(id=user)
                host = User.objects.get(id=host)
                review_instance = Review.objects.create(
                    reviewed_on=host,
                    reviewed_by=user,
                    created_by=0,
                    text=text,
                    score=score
                )
                return JsonResponse({"created": True})
            else:
                return JsonResponse({"created": False})
        return JsonResponse({"created": False})


class CreateCommentView(APIView):
    permission_classes = [AllowAny]

    # user_id, review_id, text
    def post(self, request):
        user_id = self.request.GET.get("user_id")
        user = User.objects.get(id=user_id)
        review_id = self.request.GET.get("review_id")
        text = self.request.GET.get("text")

        if user is not None and True:  # user.is_authenticated
            review = Review.objects.get(id=review_id)  # also check trip ended or not
            if review is not None:
                comment_instance = Comment.objects.create(
                    review=review,
                    user=user,
                    text=text,
                )
                return JsonResponse({"created": True})
        return JsonResponse({"created": False})


class PropartyReviewListApiView(APIView):
    permission_classes = [AllowAny]

    # proparty_id
    def get(self, request):
        data = []
        proparty_id = self.request.GET.get("proparty_id")
        property_review_list = Review.objects.filter(proparty=proparty_id)
        for review in property_review_list:
            temp = {}
            temp['user'] = str(review.reviewed_by)
            temp['text'] = review.text
            temp['score'] = review.score
            temp['created_at'] = str(review.created_at)
            temp['comments'] = []

            comment_list = Comment.objects.all()
            print(comment_list)
            for comment in comment_list:
                temp_comment = {}
                temp_comment['user'] = str(comment.user)
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
