from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import *


@receiver(post_save, sender=Student)
def create_user_profile(sender, instance, created, raw, **kwargs):
    if created and instance.role == "STUDENT":
        StudentProfile.objects.create(user=instance)
        StudentMarks.objects.create(st_mk=instance)
        
# @receiver(post_save, sender=User)
# def save_profile(sender, instance, created, raw, **kawrgs):
#     instance.StudentProfile.save()





@receiver(post_save, sender=Teacher)
def create_user_profile(sender, instance, created, raw, **kwargs):
    if created and instance.role == "TEACHER":
        TeacherProfile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()