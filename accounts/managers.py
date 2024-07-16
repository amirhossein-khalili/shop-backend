from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, phone_number, email, full_name, password):
        if phone_number:
            raise ValueError("The phone number must be set")
        if not email:
            raise ValueError("The email must be set")
        if not full_name:
            raise ValueError("username must be set the full name ")

        user = self.model(
            phone_number=phone_number,
            email=self.normalize_email(email),
            full_name=full_name,
        )
        user.set_password(password)
        user.save(using=self._db)

    def create_superuser(self, phone_number, email, full_name, password):
        user = self.create_user(phone_number, email, full_name, password)
        user.is_admin = True
        user.save(using=self._db)
