from django.db import models

# Create your models here.

class Professor(models.Model):

    

    class Meta:
        verbose_name = _("professor")
        verbose_name_plural = _("professors")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("professor_detail", kwargs={"pk": self.pk})


class Section(models.Model):

    

    class Meta:
        verbose_name = _("section")
        verbose_name_plural = _("sections")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("section_detail", kwargs={"pk": self.pk})


class Subject(models.Model):

    

    class Meta:
        verbose_name = _("subject")
        verbose_name_plural = _("subjects")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("subject_detail", kwargs={"pk": self.pk})


class Schedule(models.Model):

    

    class Meta:
        verbose_name = _("schedule")
        verbose_name_plural = _("schedules")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("schedule_detail", kwargs={"pk": self.pk})
