from mongoengine import Document, StringField, EmailField, ListField, BooleanField
import bcrypt
from django.core.mail import send_mail
import random


class User(Document):
    username = StringField(required=True, unique=True)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)
    is_admin = BooleanField(default=False)
    permissions = ListField(StringField())
    verification_code = StringField()  # إضافة الحقل verification_code
    is_verified = BooleanField(default=False)  # إضافة الحقل is_verified

    def __str__(self):
        return self.username

    def set_password(self, raw_password):
        self.password = bcrypt.hashpw(raw_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, raw_password):
        return bcrypt.checkpw(raw_password.encode('utf-8'), self.password.encode('utf-8'))

    def send_verification_code(self):
        code = str(random.randint(1000, 9999))  # كود عشوائي مكون من 4 أرقام
        self.verification_code = code
        self.save()
        send_mail(
            'كود التحقق',
            f'استخدام هذا الكود للتحقق من حسابك: {code}',
            'no-reply@myapp.com',
            [self.email],
            fail_silently=False,
        )
