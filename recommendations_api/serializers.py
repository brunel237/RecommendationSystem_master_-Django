from rest_framework import serializers
from .models import Recommendation
from posts_api.serializers import *
from users_api.serializers import *

class RecommendationSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    recommended_user = UserSerializer(required=True)
    recommended_post = PostSerializer(required=True)

    class Meta:
        model = Recommendation
        fields = ['user', 'recommended_user', 'recommended_post']