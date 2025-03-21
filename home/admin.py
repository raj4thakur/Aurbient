from django.contrib import admin
from .models import ServiceRequest, JobApplication

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "service_type", "created_at", "is_new")
    
    def is_new(self, obj):
        return not obj.reviewed  # Shows "Yes" if not reviewed
    is_new.boolean = True  # Display as a boolean (✔/✖)
    
    actions = ["mark_as_reviewed"]  # Custom action
    
    def mark_as_reviewed(self, request, queryset):
        queryset.update(reviewed=True)  # Mark selected as reviewed
        self.message_user(request, "Selected service requests marked as reviewed.")
    
    mark_as_reviewed.short_description = "Mark as Reviewed"

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "job_role", "applied_at", "is_new")
    
    def is_new(self, obj):
        return not obj.reviewed  # Shows "Yes" if not reviewed
    is_new.boolean = True  
    
    actions = ["mark_as_reviewed"]
    
    def mark_as_reviewed(self, request, queryset):
        queryset.update(reviewed=True)
        self.message_user(request, "Selected job applications marked as reviewed.")
    
    mark_as_reviewed.short_description = "Mark as Reviewed"
