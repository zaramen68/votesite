from django.contrib import admin

# Register your models here.

from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    """Choice objects can be edited inline in the Question editor."""
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    """Definition of the Question editor."""
    fieldsets = [
        # (None, {'fields': ['title']}),
        # ('type of question', {'fields': ['typeQ',]}),
        ('question', {'fields': ['question_text',]}),
        ('Date information', {'fields': ['pub_date',]}),
        # ('polls', {'fields': ['polls']}), 
        
    ]
    
    inlines = [ChoiceInline]
    list_display = ('question_text', )
    
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)