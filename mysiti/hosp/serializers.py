from django.contrib.auth import authenticate
from .models import *
from rest_framework import serializers
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'password', 'first_name', 'last_name',
                  ]
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_date):
        user = Profile.objects.create_user(**validated_date)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),

        }


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Не верный пароль или логин ")


    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),

        }





class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = '__all__'




class NewsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsImage
        fields = '__all__'




class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'



class PharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = '__all__'



class DoctorListSerializer(serializers.ModelSerializer):
    avg_rating = serializers.SerializerMethodField()


    class Meta:
        model = Doctor
        fields = ['id', 'first_name', 'last_name', 'avg_rating']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()




class DoctorDetailSerializer(serializers.ModelSerializer):
    avg_rating = serializers.SerializerMethodField()
    doctor_count = serializers.SerializerMethodField()

    class Meta:
        model = Doctor
        fields = ['avg_rating', 'doctor_count']


    def get_avg_rating(self, obj):
        return obj.get_avg_rating()


    def get_doctor_count(self, obj):
        return obj.get_doctor_count()


class PatientProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientProfile
        fields = ['id', 'first_name', 'last_name', 'blood_type', 'date_of_birth', 'allergies',
                  'phone_number', 'address']


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'status', 'date_time']


class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'



class WardsSerializer(serializers.ModelSerializer):
    patients = PatientProfileSerializer(read_only=True, many=True)
    count_patient = serializers.SerializerMethodField()


    class Meta:
        model = Wards
        fields = '__all__'


    def get_count_patient(self, obj):
        return obj.get_count_patient()






class NationalHospitalSerializer(serializers.ModelSerializer):
    # avg_rating = serializers.SerializerMethodField()
    doctor_count = serializers.SerializerMethodField()
    patient_count = serializers.SerializerMethodField()
    image = NewsImageSerializer(many=True, read_only=True)
    contact_info = ContactInfoSerializer(many=True, read_only=True)

    class Meta:
        model = NationalHospital
        fields = ['patient_count', 'doctor_count', 'pharmacy', 'doctors', 'appointment',
                  'medical_record', 'wards',
                  'news', 'address', 'instagram', 'contact_info', 'image']


    # def get_avg_rating(self, obj):
    #     return obj.get_avg_rating()
    #


    def get_doctor_count(self, obj):
        return obj.get_doctor_count()




    def get_patient_count(self, obj):
        return obj.get_patient_count()

