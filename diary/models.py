from django.db import models
from accounts.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.utils.timezone import now


class EmotionAnalysis(models.Model):
    emotion_id = models.AutoField(primary_key=True)
    happiness_score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    sadness_score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    anger_score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    hurt_score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    embarrassment_score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    anxiety_score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    summary = models.TextField(null=True, blank=True)
    reason = models.TextField()
    recommend_action = models.TextField()

    def __str__(self):
        return f"Emotion Analysis (ID: {self.emotion_id})"


class Diary(models.Model):
    diary_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='diaries')
    title = models.CharField(max_length=100, default="")  # 일기 제목
    content = models.TextField(default="")  # 일기 내용
    diary_date = models.DateField()  # 일기의 날짜
    diary_write_date = models.DateField(auto_now_add=True)  # 작성하는 날짜 -> 수정되지않음.
    emotion_analysis = models.OneToOneField(EmotionAnalysis, on_delete=models.CASCADE, related_name='diary', null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'diary_date'], name='unique_diary_per_day'),
        ]


    def __str__(self):
        return f"Diary by {self.user.id.name} on {self.diary_date}"

