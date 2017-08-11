from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Question, Choice, User

# 豪华型
# class ChoiceInline(admin.StackedInline):
# 	model = Choice
# 	extra = 3
# 紧凑型
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionAdimin(admin.ModelAdmin):
	# 1.设置排序
	# fields = ['pub_date', 'question_text']
	# 2.设置分组标题
	# fieldsets = [
	# 	(None,				{'fields': ['question_text']}),
	# 	('Date infomation',	{'fields': ['pub_date']}),
	# ]
	# 3.可展开的分组
	# fieldsets = [
	# 	(None,				{'fields': ['question_text']}),
	# 	('Date infomation',	{'fields': ['pub_date'], 'classes': ['collapse']}),
	# ]	
	# 4.在创建Question时直接添加一组Choice
	inlines = [ChoiceInline]
	# 5.修改列表内容
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	# 6.根据发布日期列展现一些搜索条件
	list_filter = ['pub_date']
	# 7.修改方法列显示信息(见models.py中was_published_recently方法的定义)
	# 8.搜索
	search_fields = ['question_text']
	# 9.另存
	# save_as = True
	pass

admin.site.register(Question, QuestionAdimin)
admin.site.register(User)

