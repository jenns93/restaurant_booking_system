from django.contrib import admin
from .models import Post, Booking_details
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

@admin.register(Booking_details)
class BookingDetailsAdmin(SummernoteModelAdmin):

    list_display = ('date', 'first_name', 'last_name', 'party_size', 'tables')
    search_fields = ['date', 'first_name', 'last_name', 'additional_information', 'allergies']
    list_filter = ('party_size', 'tables')
    summernote_fields = ('additional_information')