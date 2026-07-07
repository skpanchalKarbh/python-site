from django.contrib import admin
from .models import VisionMission, AboutUs, Event, Testimonial, Gallery, ContactMessage, ImpactCounter, Volunteer, TeamMember, Certificate

@admin.register(VisionMission)
class VisionMissionAdmin(admin.ModelAdmin):
    list_display = ('id',)

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_type', 'date', 'place', 'is_active')
    list_filter = ('event_type', 'is_active')
    search_fields = ('title', 'place')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('author', 'role', 'is_active')
    list_editable = ('is_active',)

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('caption', 'is_active')
    list_editable = ('is_active',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('name', 'email', 'phone', 'message', 'created_at')

@admin.register(ImpactCounter)
class ImpactCounterAdmin(admin.ModelAdmin):
    list_display = ('title', 'count', 'is_active', 'order')
    list_editable = ('is_active', 'order')

@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'profession', 'is_approved', 'created_at')
    list_filter = ('is_approved', 'created_at')
    search_fields = ('name', 'email', 'profession', 'message')
    list_editable = ('is_approved',)
    readonly_fields = ('name', 'email', 'phone', 'profession', 'message', 'created_at')

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'mobile_no', 'is_active', 'order')
    list_editable = ('is_active', 'order')
    search_fields = ('name', 'designation', 'mobile_no')

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'issued_by', 'is_active', 'order')
    list_editable = ('is_active', 'order')
    search_fields = ('title', 'issued_by')
