from django.contrib import admin

from .models import Question, Choice


# class ChoiceInline(admin.TabularInline):
#     model = Choice
#     extra = 3


# @admin.register(Question)
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]
#     inlines = [ChoiceInline]
#
#     list_display = ('question_text', 'pub_date', 'was_published_recently')
#     list_filter = ['pub_date']
#     search_fields = ['question_text']

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently', "get_attr")
    # fields = ('question_text', 'pub_date')
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

    list_filter = ['pub_date']
    search_fields = ['question_text']

    date_hierarchy = 'pub_date'
    # actions_on_top = True
    # actions_on_bottom = True
    # list_display_links = ('pub_date',)

    # list_editable = ('question_text',)
    list_per_page = 10


    def get_attr(self, obj):
        return 11


    # short_description = {"get_attr": "custom field"}


# admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    raw_id_fields = ("question",)
