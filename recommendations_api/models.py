from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from posts_api.models import Post, PostMedia, Like
from posts_api.serializers import PostSerializer, PostMediaSerializer
from comments_api.models import Comment
from comments_api.serializers import CommentSerializer
from users_api.serializers import *
import numpy as np
from scipy.sparse.linalg import svds
from sklearn.metrics.pairwise import cosine_similarity

class Recommendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recommended_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recommended_users', null=True, blank=True)
    recommended_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='recommended_posts', null=True, blank=True)

def create_user_user_similarity():
    likes = Like.objects.all()
    comments = Comment.objects.all()
    posts = Post.objects.all()
    users = User.objects.all()

    user_post_matrix = np.zeros((users.count(), posts.count()))
    for like in likes:
        try:
            user_id = like.author_id
            post_id = like.post_id
            user_index = list(users).index(users.get(id=user_id))
            post_index = list(posts).index(posts.get(id=post_id))
            user_post_matrix[user_index, post_index] = 1
        except ObjectDoesNotExist:
            continue

    user_comment_matrix = np.zeros((users.count(), posts.count()))
    for comment in comments:
        try:
            user_id = comment.author_id
            post_id = comment.post_id
            user_index = list(users).index(users.get(id=user_id))
            post_index = list(posts).index(posts.get(id=post_id))
            user_comment_matrix[user_index, post_index] += 1
        except ObjectDoesNotExist:
            continue

    user_user_similarity = cosine_similarity(user_post_matrix + user_comment_matrix)
    return user_user_similarity

def get_similar_users(user_id, num_users=5):
    try:
        user = User.objects.get(id=user_id)
    except ObjectDoesNotExist:
        return []

    users = User.objects.all()

    user_user_similarity = create_user_user_similarity()
    user_index = list(users).index(users.get(id=user_id))
    similar_users = np.argsort(user_user_similarity[user_index])[::-1][1:num_users+1]
    return similar_users

def recommend_users(user_id, num_recommendations=20):
    try:
        user = User.objects.get(id=user_id)
    except ObjectDoesNotExist:
        return []

    similar_users = get_similar_users(user_id, 20)
    similar_users = list(set(similar_users))
    user_likes = Like.objects.filter(author_id=user.id).values_list('post_id', flat=True)
    user_comments = Comment.objects.filter(author_id=user.id).values_list('post_id', flat=True)
    users = User.objects.all()
    recommendations = []

    for similar_user_id in similar_users:
        try:
            similar_user = list(users)[similar_user_id]
        except ObjectDoesNotExist:
            continue

        similar_user_likes = Like.objects.filter(author_id=similar_user.id).exclude(post_id__in=user_likes).values_list('post_id', flat=True)
        similar_user_comments = Comment.objects.filter(author_id=similar_user.id).exclude(post_id__in=user_comments).values_list('post_id', flat=True)

        for post_id in similar_user_likes:
            try:
                dupli = False
                for data in recommendations:
                    if data['recommended_user_id']==similar_user.id or data['recommended_post_id']==post_id:
                        dupli = True
                        break
                if not dupli:
                    recommendations.append({
                        'recommended_user_id': similar_user.id,
                        'recommended_post_id': post_id
                    })
            except ObjectDoesNotExist:
                continue
            recommendations = recommendations[:num_recommendations]


        for post_id in similar_user_comments:
            try:
                dupli = False
                for data in recommendations:
                    if data['recommended_user_id']==similar_user.id or data['recommended_post_id']==post_id:
                        dupli = True
                        break
                if not dupli:
                    recommendations.append({
                        'recommended_user_id': similar_user.id,
                        'recommended_post_id': post_id
                    })
            except ObjectDoesNotExist:
                continue
            recommendations = recommendations[:num_recommendations]

        set_user_recommendations(user_id, recommendations)
    return recommendations


def set_user_recommendations(user_id, recommendations):
    Recommendation.objects.filter(user_id=user_id).delete()
    
    for data in recommendations:
        user_list = list(Recommendation.objects.filter(user_id=user_id).values_list('recommended_user_id', flat=True))
        post_list = list(Recommendation.objects.filter(user_id=user_id).values_list('recommended_post_id', flat=True))
        if data['recommended_user_id'] in user_list and data['recommended_post_id'] in post_list:
            pass
        else:
            inst = Recommendation.objects.create(user_id=user_id, **data)
    



