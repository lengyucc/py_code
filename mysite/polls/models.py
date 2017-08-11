import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.question_text
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	was_published_recently.admin_order_field = 'pub_date'	# 根据pub_date对was_published_recently显示的数据排序
	was_published_recently.boolean = True	# 显示方式
	was_published_recently.short_description = 'Published recently?'	# 标题列名

class Choice(models.Model):
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text

class User(models.Model):
	username = models.CharField(max_length=12)
	password = models.CharField(max_length=18)
	def __str__(self):
		return self.username