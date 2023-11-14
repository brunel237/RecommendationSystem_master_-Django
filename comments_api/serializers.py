from rest_framework import serializers
from django.db.models import F
from posts_api.models import Post
from users_api.serializers import UserSerializer
from .models import Comment

#class CommentSerializer(serializers.ModelSerializer):
    
    #class Meta:
        #model = Comment
        #fields = ["post", 'content']
    
    #def create(self, validated_data):
        #post = Post.objects.get(id=validated_data["post"])
        #author = validated_data["context"].user
        #comment = Comment.objects.create(author=author, **validated_data)
        #Post.objects.filter(id=post.id).update(comment_count = F('comment_count'+1))
        #return comment

    
    #def validate(self, data):
        #content = data.get('content')
        

        
        #return data
    #def create(self, validated_data):
     #   validated_data['author'] = self.context['request'].user
      #  return 
class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(required=False)
    
    class Meta:
        model = Comment
        fields = '__all__'

    
    def validate(self, data):
        content = data.get('content')
        if content is None :
            raise serializers.ValidationError("can't make empty comment")
        return data


    def create(self, validated_data):
        post = Post.objects.get(id=validated_data['post'].id)
        author = self.context['request'].user
        comment = Comment.make_comment(post=post, author=author,  content=validated_data['content'])
        return comment
    
    
    
    
    