from django.db import models
from mentor.models import Mentor


from django.contrib.auth import get_user_model

User = get_user_model()

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    body = models.CharField(max_length=50)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.body

class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE, related_name='likes')
    is_liked = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.mentor}Liked by {self.author.name}'


class LikeComment(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='likes')
    is_liked = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.comment}Liked by{self.autor.username}'
    

class Rating(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveSmallIntegerField()
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE, related_name='ratings')
    
    def __str__(self):
        return f'{self.rating} -> {self.mentor}'
    
    
    