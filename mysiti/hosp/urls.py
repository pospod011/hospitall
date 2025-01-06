from .views import *
from rest_framework import routers
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'user', ProfileViewSet, basename='users')
router.register(r'doctor_list', DoctorListViewSet, basename='doctor_list')
router.register(r'national_hospital', NationalHospitalViewSet, basename='national_hospital')
router.register(r'contact', ContactInfoViewSet, basename='contact_info')
router.register(r'news', NewsImageViewSet, basename='news_image')
router.register(r'doctor_detail', DoctorDetailViewSet, basename='doctor_detail')
router.register(r'patient_profile', PatientProfileViewSet, basename='patient_profile')
router.register(r'pharmacy', PharmacyViewSet, basename='pharmacy')
router.register(r'appointment', AppointmentViewSet, basename='appointment')
router.register(r'medical', MedicalRecordViewSet, basename='medical')
router.register(r'feedback', FeedbackViewSet, basename='feedback')
router.register(r'wards', WardsViewSet, basename='wards')


urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # path('course/', CourseListAPIVew.as_view(), name='course_list'),
    # path('course/<int:pk>/', CourseDetailAPIVew.as_view(), name='course_detail'),
    # path('questions/', QuestionView.as_view(), name='question-list'),  # Получение вопросов или создание нового
    # path('check_answer/', CheckAnswerView.as_view(), name='check-answer'),  # Проверка ответа
    # path('register/', RegisterView.as_view(), name='register'),
    # path('login/', CustomLoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
]
