from django.db import models
from django.utils.translation import gettext as _


# Create your models here.

class Professor(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_initial = models.CharField(max_length=50)

    class Meta:
        verbose_name = _("professor")
        verbose_name_plural = _("professors")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("professor_detail", kwargs={"pk": self.pk})

    @property
    def full_name_last_name_first(self):
        return self.last_name + ', ' + self.first_name + ' ' + self.middle_initial + '.'


class Section(models.Model):

    year_level = models.PositiveSmallIntegerField()
    section = models.CharField(max_length=2)

    class Meta:
        verbose_name = _("section")
        verbose_name_plural = _("sections")

    def __str__(self):
        return self.year_level + self.section

    def get_absolute_url(self):
        return reverse("section_detail", kwargs={"pk": self.pk})


class Subject(models.Model):

    subject_code = models.CharField(_(""), max_length=50)
    subject_description = models.CharField(_(""), max_length=200)

    class Meta:
        verbose_name = _("subject")
        verbose_name_plural = _("subjects")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("subject_detail", kwargs={"pk": self.pk})


class Schedule(models.Model):

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    SESSION_TYPE_CHOICES = [
        ('Lec', 'Lecture'),
        ('Lab', 'Laboratory'),
    ]
    session_type = models.CharField(max_length=50, choices=SESSION_TYPE_CHOICES)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    DAYS_OF_WEEK = [
        ('M', 'Monday'),
        ('T', 'Tuesday'),
        ('W', 'Wednesday'),
        ('TH', 'Thursday'),
        ('F', 'Friday'),
        ('SA', 'Saturday'),
        ('S', 'Sunday'),
    ]
    days = models.CharField(max_length=50, choices=DAYS_OF_WEEK)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        verbose_name = _("schedule")
        verbose_name_plural = _("schedules")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("schedule_detail", kwargs={"pk": self.pk})
