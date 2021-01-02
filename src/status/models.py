from django.contrib.auth.models import User
from django.db import models
import datetime
from django.core.exceptions import ValidationError

today = datetime.date.today()

# Create your models here.


def upload_status_img(instance, filename):
    return f"updates/{instance.user}/{filename}"


class StatusQuerySet(models.QuerySet):
    pass


class StatusManager(models.Manager):
    def get_queryset(self):
        return StatusQuerySet(self.model, using=self._db)


def no_future(date_value):
    if date_value > today:
        raise ValidationError("Status date  cannot be in the future.")


def no_past(date_value):
    if date_value < today:
        raise ValidationError("Status date  cannot be in the PAST.")


def today_validation(date_value):
    if date_value != today:
        raise ValidationError('Status date must be today date !')


class Status(models.Model):  # fb status, instgram post, tweet, linkedin post
    # setting.AUTH_USER_MODEL = User
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="statuses")
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_status_img, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    date = models.DateField(validators=[today_validation])

    objects = StatusManager()

    class Meta:
        ordering = ("-pk",)  # ordering desc pk
        verbose_name = 'New Status Post'  # shown at "add" new object btn
        verbose_name_plural = 'Status Posts'  # shown as "model name" under "app name"

    def __str__(self):
        return self.content[:50]

    # def save(self, *args, **kwargs):
    #     if self.date < today:
    #         raise ValidationError("The date cannot be in the past!")
    #
    #     if self.date > today:
    #         raise ValidationError("The date cannot be in the future!")
    #     super(Status, self).save(*args, **kwargs)