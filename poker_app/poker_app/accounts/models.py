from django.contrib.auth import models as auth_models, get_user_model
from django.core.validators import MinLengthValidator, MaxValueValidator

from django.db import models

from poker_app.web.managers import PokerUserManager
from poker_app.web.validators import validate_only_letters

'''
1. Create model extending ...
2. Configure this model in settings.py
3. Create user manager
'''

UserModel = get_user_model()


# TODO: 'ADD auth_models.PermissionsMixin to the PokerUser'


class PokerUser(auth_models.AbstractBaseUser):  # auth_models.PermissionsMixin
    USERNAME_MAX_LENGTH = 25

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        unique=True,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'username'

    objects = PokerUserManager()


class Profile(models.Model):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30

    #
    # first_name = models.CharField(
    #     max_length=FIRST_NAME_MAX_LENGTH,
    #     validators=(
    #         MinLengthValidator(FIRST_NAME_MIN_LENGTH),
    #         validate_only_letters,
    #     )
    # )
    #
    # last_name = models.CharField(
    #     max_length=LAST_NAME_MAX_LENGTH,
    #     validators=(
    #         MinLengthValidator(LAST_NAME_MIN_LENGTH),
    #         validate_only_letters,
    #     )
    # )
    #
    # picture = models.URLField()
    #
    # date_of_birth = models.DateField(
    #     null=True,
    #     blank=True,
    # )
    #
    # slogan = models.TextField(
    #     null=True,
    #     blank=True,
    # )

    email = models.EmailField(
        null=True,
        blank=True,
    )

    # user = models.OneToOneField(
    #     PokerUser,
    #     on_delete=models.CASCADE,
    #     # primary_key=True,
    # )

    # def __str__(self):
    #     return f'{self.first_name} {self.last_name}'


