from rest_framework import generics, status, viewsets
from .serializers import *
from rest_framework import generics, permissions
from rest_framework.response import Response
from comments_api.serializers import *

class RecommendationViewSet(viewsets.ModelViewSet):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticated]

    def recommendation_list(self, request, id=None):
        try:
            # user = User.objects.get(id=id)
            recommend = Recommendation.objects.filter(user_id=id)
            recommendation_serializer = RecommendationSerializer(recommend, many=True)
            temp = recommendation_serializer.data
            for slz_data in temp:
                post = slz_data["recommended_post"]["id"]
                
                try:
                    media_obj = PostMedia.objects.get(post_id=post)
                    media = PostMediaSerializer(media_obj)
                    slz_data["recommended_post"]["media"] = media.data
                except Exception as e:
                    slz_data["recommended_post"]["media"] = []

                comments = Comment.objects.filter(post_id=post)
                cmt = CommentSerializer(comments, many=True)
                slz_data["recommended_post"]["comments"] = cmt.data
                

            return Response({"success": True, "message": recommendation_serializer.data})
        except Exception as e:
            return Response({"success": False, "message": f"failed to load recommendations for user {id} :"+str(e)}, status=400)

    # def post_list(self, request, id=None):
    #     pass 