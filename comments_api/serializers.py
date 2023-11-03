from rest_framework import serializers
from django.db.models import F
from posts_api.models import Post
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
    author = serializers.ReadOnlyField(source='get_user_id')  # Champ en lecture seule
    
    class Meta:
        model = Comment
        fields = ['author', 'post', 'content',]

    
    def validate(self, data):
        author = data.get('author')
        post = data.get('post')
        content = data.get('content')
        if content is None :
            raise serializers.ValidationError("can't make empty comment")


        return data
    
    def create(self, validated_data):
        post = validated_data['post']
        author = self.context['request'].user
        comment = Comment.objects.create(author=author, **validated_data)
        post.comment_count = F('comment_count')+ 1 # Incrémente comment_count du Post
        post.save()
        return comment
    
    
    
    
    