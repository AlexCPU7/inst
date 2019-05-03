from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.core.mail import send_mail
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email, and password.
        """
        if not email:
            raise ValueError('email должен быть указан')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Суперпользователь должен иметь is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Суперпользователь должен иметь is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    password are required. Other fields are optional.
    """
    GENDER_GROUP = (
        ('man', _('Мужчина')),
        ('women', _('Женщина'))
    )

    first_name = models.CharField(_('Имя'), max_length=30)
    last_name = models.CharField(_('Фамилия'), max_length=30)
    email = models.EmailField(_('Электронная почта'), unique=True)
    date_birth = models.DateField(_('Дата рождения'))
    phone = models.CharField(_('Номер телефона'), max_length=12, blank=True, null=True)
    gender = models.CharField(_('Пол'), choices=GENDER_GROUP, blank=True, null=True, max_length=5)
    is_staff = models.BooleanField(
        _('Доступ к админке'),
        default=False,
        help_text=_('Указывает, может ли пользователь войти на этот сайт администратора.'),
    )
    is_active = models.BooleanField(
        _('Активность'),
        default=True,
        help_text=_('Активный пользователь'),
    )
    date_joined = models.DateTimeField(_('Дата присоединения'), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_birth']

    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the last_name plus the first_name, with a space in between.
        """
        full_name = '%s %s' % (self.last_name, self.first_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)
