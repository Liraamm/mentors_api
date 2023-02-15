from rest_framework import serializers
from .models import Like, Comment, LikeComment, Rating


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')
    class Meta:
        model = Comment
        fields = '__all__'
        
    def create(self, validated_data):
        request = self.context.get('request')
        print(self.context.get('request'))
        user = request.user
        comment = Comment.objects.create(author=user, **validated_data)
        return comment
        

class RatingSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')
    
    class Meta:
        model = Rating
        fields = '__all__'
    
    def validate_rating(self, rating):
        if rating not in range(1, 6):
            raise serializers.ValidationError('Рейтинг не может быть больше 5 и меньше 0')
        return rating
        
    def validate_mentor(self, mentor):
        if self.Meta.model.objects.filter(mentor=mentor).exists():
            raise serializers.ValidationError('Вы уже оставляли рейтинг на данного ментора')
        return mentor
    
    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        rating = Rating.objects.create(author=user, **validated_data)
        return rating
    

class LikeSerializer(serializers.ModelSerializer):
    mentor = serializers.ReadOnlyField()
    author = serializers.ReadOnlyField(source='author.email')
    
    class Meta:
        model = Like
        fields = '__all__'
    
    def create(self, **validated_data):
        request = self.context.get('request')
        user = request.user
        like = Like.objects.create(author=user, **validated_data)
        return like
    

class LikeCommentSerializer(serializers.ModelSerializer):
    comment = serializers.ReadOnlyField()
    author = serializers.ReadOnlyField(source='author.email')
    
    class Meta:
        model = LikeComment
        fields = '__all__'
        
    def create(self, **validated_data):
        request = self.context.get('request')
        user = request.user
        like_comment = LikeComment.objects.create(author=user, **validated_data)
        return like_comment
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['likes_count'] = instance.likes.count()
        