from django.apps import AppConfig
from django.contrib.auth.hashers import make_password
from django.conf import settings


class ApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "api"

    def ready(self):
        from .models import User

        if (
            settings.ADMIN_EMAIL
            and not User.objects.filter(email=settings.ADMIN_EMAIL).exists()
        ):
            User.objects.create(
                name=settings.ADMIN_NAME,
                email=settings.ADMIN_EMAIL,
                phone_number=settings.ADMIN_PHONE,
                password=make_password(settings.ADMIN_PASSWORD),
                is_superuser=True,
                is_staff=True,
                is_active=True,
            )


