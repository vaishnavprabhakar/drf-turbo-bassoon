from django.contrib import admin
from app1.models import Snippet
# Register your models here.


class SnippetAdmin(admin.ModelAdmin):

    list_display = ['title', 'created', 'code','linenos', 'language', 'style']

    