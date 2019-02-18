from rest_framework.serializers import ModelSerializer

<<<<<<< HEAD
from .models import Review

class ReviewListSerializer(ModelSerializer):
	class Meta:

		model = Review
		fields = [
		'trip',
		'user_review',
		'user_score',

 


		]
=======
>>>>>>> 9d11ff4c22cddaa12f123e7190c95d519dee348d
