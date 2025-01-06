
from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


class ContactInfoInline(admin.TabularInline):
    model = ContactInfo
    extra = 1


class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 1






@admin.register(NationalHospital)
class AllAdmin(TranslationAdmin):
    inlines = [ContactInfoInline, NewsImageInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }



@admin.register(MedicalRecord, Feedback, Wards, Pharmacy)
class AllAdmin(TranslationAdmin):

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }





admin.site.register(Profile)
admin.site.register(StoreReview)
admin.site.register(PatientProfile)
admin.site.register(Doctor)
admin.site.register(Appointment)

