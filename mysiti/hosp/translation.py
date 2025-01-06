from .models import NationalHospital, MedicalRecord, Feedback, Wards, Pharmacy
from modeltranslation.translator import TranslationOptions, register

@register(NationalHospital)
class ProductTranslationOptions(TranslationOptions):
    fields = ('address', 'news')


@register(MedicalRecord)
class ProductTranslationOptions(TranslationOptions):
    fields = ('diagnosis', 'treatment')


@register(Feedback)
class ProductTranslationOptions(TranslationOptions):
    fields = ('comment',)


@register(Wards)
class ProductTranslationOptions(TranslationOptions):
    fields = ('ward_name',)


@register(Pharmacy)
class ProductTranslationOptions(TranslationOptions):
    fields = ('description',)


