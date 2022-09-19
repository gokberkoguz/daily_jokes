import uuid
from datetime import datetime, timedelta

import jwt
import pytz
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.core import exceptions
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from utility_app.lib.constants import SYSTEM_TIMEZONE


class UserManager(BaseUserManager):
    """Custom User Manager"""

    def create_user(self, email, password):
        """Create and return a `User` with an email and password."""
        if email is None:
            raise TypeError("Users must have an email")
        if password is None:
            raise TypeError("Users must have a password")

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password):
        """
        Create and return a `User` with powers.
        Superuser is an admin that can do anything.
        """
        if password is None:
            raise TypeError("Super")

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom User Class that overrides Django Auth User."""

    # We do not want to use an username
    username = None

    first_name = models.CharField(_("first name"), max_length=30, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)

    # Each `User` needs a unique email to identify itself
    # Email is also a way to contact the user
    email = models.EmailField(db_index=True, unique=True)

    # When user no-longer exists deactivate.
    # This way you do not have to delete the user
    is_active = models.BooleanField(default=True)

    # The `is_staff` flag is expected by Django to determine who can and cannot
    # log into the Django admin site. For most users, this flag will always be
    # false.
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    # Password reset fields
    reset_password_token = models.UUIDField(null=True)
    reset_password_token_expires_at = models.DateTimeField(null=True)
    reset_password_sent_at = models.DateTimeField(null=True)

    # The `USERNAME_FIELD` property tells us which field we will use to log in.
    # In this case, we want that to be the email field.
    USERNAME_FIELD = "email"

    # Tells Django that the UserManager class should manage
    # objects of this type.
    objects = UserManager()

    def __str__(self):
        """Use email to stringify user"""
        return self.email

    def get_username(self):
        """User email is also username."""
        return self.email

    def generate_jwt_token(
        self,
        first_issued_at=datetime.now(),
        expire_time=settings.JWT_ACCESS_TOKEN_EXP_TIME,
    ):
        """
        Generates a JSON Web Token that encodes user and
        has an expiration date set to JWT_ACCESS_TOKEN_EXP_TIME.

        Heads up! Does not invalidate previous non-expired tokens!
        """
        dt = datetime.now() + timedelta(seconds=expire_time)
        issued_at = datetime.now()
        token = jwt.encode(
            {
                "id": self.pk,
                "exp": int(dt.strftime("%s")),
                "first_iat": int(first_issued_at.strftime("%s")),
                "iat": int(issued_at.strftime("%s")),
            },
            settings.SECRET_KEY,
            algorithm="HS256",
        )

        return token.decode("utf-8")

    def generate_password_token(self):
        """
        Generates reset password token for the user.
        Also, sets reset_password_token_expires_at, reset_password_sent_at.
        :return: reset_password_token
        """
        self.reset_password_token = uuid.uuid4().hex
        self.reset_password_token_expires_at = datetime.now(pytz.utc) + timedelta(
            days=1
        )
        self.reset_password_sent_at = datetime.now(pytz.utc) + SYSTEM_TIMEZONE
        self.save()
        return self.reset_password_token

    def clear_password_token(self):
        """Clears password token and its expiration date"""
        self.reset_password_token = None
        self.reset_password_token_expires_at = None
        self.save()

    def update_password(self, raw_password):
        """Secure password update."""
        self.set_password(raw_password)
        self.save()

    @staticmethod
    def find_by_reset_password_token(reset_password_token):
        """
        Finds User by reset password token
        :return: User if exists and token is valid, otherwise None
        """
        try:
            user = User.objects.get(reset_password_token=reset_password_token)
            # check if token expired
            if user.reset_password_token_expires_at < datetime.now(pytz.utc):
                user = None
        except (User.DoesNotExist, exceptions.ValidationError):
            user = None

        return user
