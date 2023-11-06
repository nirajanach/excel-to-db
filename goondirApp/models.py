from django.db import models
from django.contrib.auth.models import User

from goondirApp.middleware import current_user
# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=20)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES, null=True, blank = True)
    phone_number = models.IntegerField(max_length=10)
    DOB = models.DateField()
    address = models.CharField(max_length=150)
    medicare_number = models.IntegerField(max_length=11)
    created_at = models.DateTimeField(auto_now_add=True,blank = True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, editable=False,
                                   default=current_user.get_current_user)
    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'medicare_number', 'DOB',)
    # def __str__(self):
    #     return self.firstName+ " "+self.lastName

class Survey(models.Model):
    first_survey_date = models.DateField()
    survey_status = models.CharField(max_length=20)
    start_of_VHS = models.DateField()
    VHS_family = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, editable=False,
                                   default=current_user.get_current_user)
    def __str__(self):
        return self.survey_status+ " "+self.VHS_family
class Oxymeter(models.Model):
    pulse_oxymeter_ID = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, editable=False,
                                   default=current_user.get_current_user)
    def __str__(self):
        return self.pulse_oxymeter_ID


class BpMonitor(models.Model):
    bp_ID = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, editable=False,
                                   default=current_user.get_current_user)
    def __str__(self):
        return self.bp_ID


class BloodGlucoseMonitor(models.Model):
    blood_glucose_ID = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, editable=False,
                                   default=current_user.get_current_user)
    def __str__(self):
        return self.blood_glucose_ID


class WeighScale(models.Model):
    weigh_scale_ID = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, editable=False,
                                   default=current_user.get_current_user)
    def __str__(self):
        return self.weigh_scale_ID

class Tablet(models.Model):
    tablet_serial_ID = models.CharField(max_length=15)
    tablet_imei = models.IntegerField(max_length=15)
    sim_number = models.IntegerField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, editable=False,
                                   default=current_user.get_current_user)
    def __str__(self):
        return self.tablet_serial_ID

class MedicalBranch(models.Model):
    branch_name = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, editable=False,
                                   default=current_user.get_current_user)
    def __str__(self):
        return self.branch_name

class PatientDeviceInformation(models.Model):
    patient_ID = models.ForeignKey(
        Patient, on_delete=models.CASCADE)
    bp_monitor_ID = models.ForeignKey(
        BpMonitor, on_delete=models.CASCADE)
    blood_glucose_monitor = models.ForeignKey(
        BloodGlucoseMonitor, on_delete=models.CASCADE)
    oxymeter_ID = models.ForeignKey(
        Oxymeter, on_delete=models.CASCADE)
    weigh_scale_ID = models.ForeignKey(
        WeighScale, on_delete=models.CASCADE)
    medical_branch_ID = models.ForeignKey(
        MedicalBranch, on_delete=models.CASCADE)
    tablet_ID = models.ForeignKey(
        Tablet, on_delete=models.CASCADE)
    survey_ID = models.ForeignKey(
        Survey, on_delete=models.CASCADE)
    # User = models.ForeignKey(
    #     User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, editable=False,
                                   default=current_user.get_current_user)
