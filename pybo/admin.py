from django.contrib import admin

from pybo.models import Question

# Register your models here.


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']
    list_display = ['id', 'subject', 'content', 'create_date']
    list_filter = ['subject']
    list_per_page = 3


admin.site.register(Question, QuestionAdmin)
