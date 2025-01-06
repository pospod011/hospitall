from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField



class NationalHospital(models.Model):
    hospital_name = models.CharField(max_length=43)
    pharmacy = models.URLField(null=True, blank=True)
    doctors = models.URLField(null=True, blank=True)
    appointment = models.URLField(null=True, blank=True)
    medical_record = models.URLField(null=True, blank=True)
    wards = models.URLField(null=True, blank=True)
    address = models.TextField(blank=True, null=True)
    instagram = models.URLField(null=True, blank=True)
    news = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.hospital_name}'

    # def get_avg_rating(self):
    #     ratings = self.hospital_review.all()
    #     if ratings.exists():
    #         return round(sum(i.rating for i in ratings) / ratings.count(), 1)
    #     return 0
    #


    def get_doctor_count(self):
        doctors = self.doctor_hospital.filter(role='врач')
        return doctors.count()




    def get_patient_count(self):
        patient = self.patient_hospital.filter(role='пациент')
        return patient.count()





class ContactInfo(models.Model):
    contact_info = PhoneNumberField()
    national = models.ForeignKey(NationalHospital, on_delete=models.CASCADE, related_name='contacts')


    def __str__(self):
        return f'{self.national}, {self.contact_info}'


class NewsImage(models.Model):
    national_hospital = models.ForeignKey(NationalHospital, on_delete=models.CASCADE, related_name='news_hospital')
    image = models.ImageField(upload_to='news_image/', null=True, blank=True)



class Profile(AbstractUser):
    ROLE_CHOICES = [
        ('администратор', 'администратор'),
        ('пациент', 'пациент'),
        ('врач', 'врач'),
    ]

    role = models.CharField(max_length=43, choices=ROLE_CHOICES, default='пациент')
    phone_number = PhoneNumberField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_image/', null=True, blank=True)
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateTimeField(blank=True, null=True)


class Doctor(Profile):
    national_hospital = models.ForeignKey(NationalHospital, on_delete=models.CASCADE, related_name='doctor_hospital')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='doctor_profile')
    SPECIALTY_CHOICES = [
        ('Врач-кардиолог', 'Врач-кардиолог'),
        ('Врач-отоларинголог', 'Врач-отоларинголог'),
        ('Врач-терапевт', 'Врач-терапевт'),
        ('Врач-терапевт госпитального отделения', 'Врач-терапевт госпитального отделения'),
        ('Врач мануальной терапии', 'Врач мануальной терапии'),
        ('Врач-рефлексотерапевт-невролог', 'Врач-рефлексотерапевт-невролог'),
        ('Врач-психиатр', 'Врач-психиатр'),
        ('Врач-психиатр-нарколог', 'Врач-психиатр-нарколог'),
        ('Врач-гематолог', 'Врач-гематолог'),
        ('Врач-ревматолог', 'Врач-ревматолог'),
        ('Врач-офтальмолог', 'Врач-офтальмолог'),
        ('Врач-уролог', 'Врач-уролог'),
        ('Врач-акушер-гинеколог', 'Врач-акушер-гинеколог'),
        ('Врач-дерматовенеролог', 'Врач-дерматовенеролог'),
        ('Врач-функциональной диагностики', 'Врач-функциональной диагностики'),
        ('Фельдшер военно-врачебной комиссии', 'Фельдшер военно-врачебной комиссии'),
        ('Медицинская сестра военно-врачебной комиссии', 'Медицинская сестра военно-врачебной комиссии'),
        ('Медицинская сестра хирургического отделения', 'Медицинская сестра хирургического отделения'),
        ('Медицинская сестра отоларингологического отделения', 'Медицинская сестра отоларингологического отделения'),
        ('Медицинская сестра процедурного кабинета', 'Медицинская сестра процедурного кабинета'),
        ('Медицинская сестра неврологического отделения', 'Медицинская сестра неврологического отделения'),
        ('Медицинская сестра кожно-венерологического отделения', 'Медицинская сестра кожно-венерологического '
                                                                 'отделения'),
        ('Медицинская сестра диспансерного отделения', 'Медицинская сестра диспансерного отделения'),
        ('Медицинская сестра консультативногоотделения', 'Медицинская сестра консультативногоотделения'),
        ('Медицинская сестра палатная (постовая) госпитальногоотделения', 'Медицинская сестра палатная (постовая) '
                                                                          'госпитальногоотделения'),
        ('Медицинская сестра физиотерапевтического отделения', 'Медицинская сестра физиотерапевтического отделения'),
        ('Медицинская сестра отделения функциональной диагностики', 'Медицинская сестра отделения функциональной '
                                                                    'диагностики'),
        (' Рентгенолаборант', ' Рентгенолаборант'),
        ('Медицинский регистратор', 'Медицинский регистратор'),
        ('Санитарка хирургического отделения', 'Санитарка хирургического отделения'),
    ]
    specialty = models.CharField(max_length=300, choices=SPECIALTY_CHOICES,)
    department = models.CharField(max_length=43)
    experience = models.DateField(verbose_name='опыт работы')
    shift_start = models.DateTimeField(auto_now_add=True)
    shift_end = models.DateField(auto_now=True)
    WORKING_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
    working_days = MultiSelectField(max_length=43, max_choices=4, choices=WORKING_CHOICES,)
    price = models.PositiveIntegerField(default=0)


    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors_Profile"


    def get_avg_rating(self):
        ratings = self.doctor_feedback.all()
        if ratings.exists():
            return round(sum(i.rating for i in ratings) / ratings.count(), 1)
        return 0



    # def get_doctor_count(self):
    #     doctors = self.doctor_profile.filter(role='врач')
    #     return doctors.count()
    #



# функция которая доктор болуп регистрация болгондорду санайт

class PatientProfile(Profile):
    national_hospital = models.ForeignKey(NationalHospital, on_delete=models.CASCADE, related_name='patient_hospital')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='patients')
    emergency_contact = models.CharField(max_length=98, blank=True, null=True)
    BLOOD_CHOICES = [
        ('Бомбейский фенотип (hh)', 'Бомбейский фенотип (hh)'),
        ('Золотая кровь (Rh-нулевой)', 'Золотая кровь (Rh-нулевой)'),
        ('Группа крови О−', 'Группа крови О−'),
        ('Группа крови О+', 'Группа крови О+'),
        ('Группа крови А−', 'Группа крови А−'),
        ('Группа крови А+', 'Группа крови А+'),
        ('Группа крови Б−', 'Группа крови Б−'),
        ('Группа крови В+', 'Группа крови В+'),
        ('Группа крови АБ−', 'Группа крови АБ−'),
        ('Группа крови АБ+', 'Группа крови АБ+'),
    ]
    blood_type = MultiSelectField(max_length=43, max_choices=2, choices=BLOOD_CHOICES,)
    allergies = models.CharField(max_length=99, null=True, blank=True)

    class Meta:
        verbose_name = "PatientProfile"
        verbose_name_plural = "Patient_Profile"

# функция которая доктор болуп регистрация болгондорду санайт



class Pharmacy(models.Model):
    product_name = models.CharField(max_length=32)
    product_image = models.ImageField(upload_to='product_image/')
    price = models.PositiveSmallIntegerField()
    description = models.TextField()
    hospital = models.ForeignKey(NationalHospital, on_delete=models.CASCADE, related_name='hospital_product')


    def __str__(self):
        return f'{self.product_name}, {self.hospital}'



class Appointment(models.Model): #назначение
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name='patient_appoint')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctor_appoint')
    date_time = models.DateTimeField()
    STATUS_CHOICES = [
        ('запланировано', 'запланировано'),
        ('завершено', 'завершено'),
        ('отменено', 'отменено'),
    ]

    status = models.CharField(max_length=80, choices=STATUS_CHOICES, default='запланировано')


class MedicalRecord(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name='patient_record')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctor_record')
    diagnosis = models.CharField(max_length=43)
    treatment = models.CharField(max_length=43)
    prescribed_medication = models.CharField(max_length=43)
    created_at = models.DateTimeField()


class StoreReview(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name='patient_review')
    national_hospital = models.ForeignKey(NationalHospital, on_delete=models.CASCADE, related_name='hospital_review')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    command = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.patient}, {self.national_hospital}, {self.rating}'



class Feedback(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctor_feedback')
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name='patient_feedback')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)



class Wards(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name='wards_patient')
    national_hospital = models.ForeignKey(NationalHospital, on_delete=models.CASCADE, related_name='wards_hospital')
    ward_name = models.CharField(max_length=32)
    capacity = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name='кол в полате')
    WARD_CHOICES = [
        ('simple', 'simple'),
        ('vip', 'vip'),
    ]
    ward_type = models.CharField(max_length=23, choices=WARD_CHOICES, default='simple')

    def get_count_patient(self):
        patients = self.wards_patient
        return patients.count()


    def get_total_capacity(self):
        return self.capacity - self.get_count_patient()


# функция канча адам бар экенин жана канча места бош экенин эсептеп койот



class Chat(models.Model):
    person = models.ManyToManyField(Profile)
    created_date = models.DateField(auto_now_add=True)


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    auther = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='message_image/', null=True, blank=True)
    video = models.FileField(upload_to='message_video/', null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)


