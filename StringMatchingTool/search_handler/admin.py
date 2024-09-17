# admin.py
from django.contrib import admin
from .models import FileProcessingResult

@admin.register(FileProcessingResult)
class FileProcessingResultAdmin(admin.ModelAdmin):
    list_display = ('result_id', 'query', 'results')
    search_fields = ('result_id', 'query')
