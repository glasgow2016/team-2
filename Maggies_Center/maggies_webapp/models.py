from __future__ import unicode_literals
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

import json


class StaffMember(models.Model):
    STAFF_TYPE_CHOICES = (
        ("CH", "Centre Head"),
        ("CS", "CSS"),
        ("PS", "Psychologist"),
        ("BA", "Benefits advisor"),
        ("FR", "Fundraiser"),
        ("SS", "Sessional Staff"),
    )

    user_mapping = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    surname = models.CharField(max_length=120)
    staff_type = models.CharField(max_length=2, choices=STAFF_TYPE_CHOICES)


class Language(models.Model):
    name = models.CharField(max_length=40)
    name_in_english = models.CharField(max_length=30)


class Centre(models.Model):
    name = models.CharField(max_length=100)
    language = models.ForeignKey(Language, on_delete=models.PROTECT)


class ActivityName(models.Model):
    lang = models.ForeignKey(Language, on_delete=models.CASCADE)
    translated_name = models.CharField(max_length=100)


class Activity(models.Model):
    name = models.ForeignKey(ActivityName, on_delete=models.CASCADE)
    centre = models.ForeignKey(Centre, on_delete=models.CASCADE)
    instructed_by = models.ManyToManyField(StaffMember)
    scheduled_times_json = models.CharField(max_length=2000)
    timestamp = models.DateTimeField()

    def save(self, *args, **kwargs):
        self.scheduled_times_json = json.dumps(self.scheduled_times_array)
        if self.pk is None:
            self.timestamp = now()
        super(Activity, self).save(*args, **kwargs)

    def get_scheduled_times(self, day_of_week):
        """
        Get scheduled times for a given day of week
        :param day_of_week: 0-indexed day of week, Mon-Sun
        :return: Array of 2-tuples containing starting and ending times for
                 given day
        """
        if day_of_week < 0 or day_of_week > 6:
            raise ValueError("Day of week must be between 0 - Mon and 6 - Sun")
        return self.scheduled_times_array[day_of_week]

    def set_scheduled_times(self, day_of_week, times):
        """
        Set scheduled times for a given day of week
        :param day_of_week: 0-indexed day of week, Mon-Sun
        :param times Array of 2-tuples containing starting and ending times for
                     given day
        :return: None
        """
        if day_of_week < 0 or day_of_week > 6:
            raise ValueError("Day of week must be between 0 - Mon and 6 - Sun")
        self.scheduled_times_array[day_of_week] = times
        self.save()

    def __init__(self, *args, **kwargs):
        super(Activity, self).__init__(*args, **kwargs)
        self.scheduled_times_array = json.loads(self.scheduled_times_json)
        

class Visit(models.Model):
    GENDER_CHOICES = (
        ("MA", "Male"),
        ("FE", "Female"),
        ("UM", "Under 18 Male"),
        ("UF", "Under 18 Female")
    )
    JOURNEY_CHOICES = (
        ("PW", "PwC"),
        ("CA", "Carer"),
        ("PR", "Professional"),
        ("AR", "Architectural"),
        ("IN", "International"),
        ("OV", "Other visitor")
    )
    CANCER_TYPE_CHOICES = (
        ("BR", "Brain / CNS"),
        ("GY", "Gynae"),
        ("HN", "Head / Neck"),
        ("HA", "Haemat"),
        ("LI", "Liver"),
        ("LO", "Lower GI"),
        ("LU", "Lung"),
        ("PA", "Pancreatic"),
        ("PR", "Prostate"),
        ("RA", "Rare"),
        ("SA", "Sarcoma"),
        ("SK", "Skin / Mel"),
        ("TE", "Testicular"),
        ("UK", "Unknown Primary"),
        ("UG", "Upper GI"),
        ("UR", "Urolog"),
        ("NS", "Not stated")
    )
    VISIT_NATURE_CHOICES = (
        ("BO", "Booked"),
        ("DI", "Drop - In"),
        ("PR", "Programme"),
        ("EM", "E-mail support"),
        ("FR", "Fundraising"),
        ("OR", "Outreach"),
        ("TP", "Telephone support"),
    )
    VISIT_TYPE_CHOICES = (
        ("NE", "New"),
        ("RE", "Returning")
    )

    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    journey_stage = models.CharField(max_length=2, choices=JOURNEY_CHOICES)
    visit_site = models.ForeignKey(Centre, on_delete=models.CASCADE)
    nature_of_visit = models.CharField(max_length=2,
                                       choices=VISIT_NATURE_CHOICES)
    cancer_site = models.CharField(max_length=2, choices=CANCER_TYPE_CHOICES)
    seen_by = models.ForeignKey(StaffMember, on_delete=models.SET_NULL,
                                null=True)
    type = models.CharField(max_length=2, choices=VISIT_TYPE_CHOICES)
    activities = models.ManyToManyField(Activity)


class TempVisitNameMapping(models.Model):
    visitor_name = models.CharField(max_length=100)
    related_visit = models.ForeignKey(Visit, on_delete=models.CASCADE)
