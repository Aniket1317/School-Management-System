from django.contrib import admin
from .models import Student,OnlineClass, OnlineTest

class OnlineClassAdmin(admin.ModelAdmin):
	list_display = ['std', 'sub', 'c_date', 'c_day', 'teacher_name']
	search_fields = ['std','teacher_name','c_day']
	list_filter = ['std', 'sub','teacher_name']
	class Meta:
		model = OnlineClass

admin.site.register(Student)
admin.site.register(OnlineClass, OnlineClassAdmin)
admin.site.register(OnlineTest)
