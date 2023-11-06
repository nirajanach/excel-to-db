from django.contrib import admin
from django.contrib.admin import AdminSite
from django.conf.urls import url
from django.urls import path
from django.conf.urls import include
from django.contrib.auth.models import Group
from django.conf.urls import url
from import_export.admin import ImportExportModelAdmin
from import_export import resources, widgets
from import_export.fields import Field
from .models import *
from goondirApp.views import upload_xls
# Register your models here.
class PatientAdmin(ImportExportModelAdmin):
    exclude = ('created_at',)
    readonly_fields = ()
    sortable_by = 'id'
    date_hierarchy = 'created_at'
    list_display = ('name', 'DOB', 'phone_number', 'medicare_number', 'address')
    list_filter = ('gender',)
    search_fields = ('name', 'DOB', 'phone_number', 'medicare_number', 'address')
    fields = ('name', 'DOB', 'phone_number', 'medicare_number', 'address')


class SurveyAdmin(ImportExportModelAdmin):
    exclude = ('created_at',)
    fields = ()
    readonly_fields = ()
    sortable_by = 'id'
    date_hierarchy = 'created_at'
    list_display = ('first_survey_date', 'survey_status', 'start_of_VHS', 'VHS_family')
    list_filter = ('survey_status',)
    search_fields = ('first_survey_date', 'survey_status', 'start_of_VHS', 'VHS_family')

class MedicalBranchAdmin(ImportExportModelAdmin):
    exclude = ('created_at',)
    fields = ()
    readonly_fields = ()
    sortable_by = 'id'
    date_hierarchy = 'created_at'
    list_display = ('branch_name',)
    search_fields = ('branch_name',)

class TabletAdmin(ImportExportModelAdmin):
    exclude = ('created_at',)
    fields = ()
    readonly_fields = ()
    sortable_by = 'id'
    date_hierarchy = 'created_at'
    list_display = ('tablet_serial_ID', 'tablet_imei', 'sim_number')
    list_filter = ('tablet_imei',)
    search_fields = ('tablet_Serial_ID', 'tablet_imei', 'sim_number')

class OxymeterAdmin(ImportExportModelAdmin):
    exclude = ('created_at',)
    fields = ()
    readonly_fields = ()
    sortable_by = 'id'
    date_hierarchy = 'created_at'
    list_display = ('pulse_oxymeter_ID',)

    search_fields = ('pulse_oxymeter_ID',)

class BpMonitorAdmin(ImportExportModelAdmin):
    exclude = ('created_at',)
    fields = ()
    readonly_fields = ()
    sortable_by = 'id'
    date_hierarchy = 'created_at'
    list_display = ('bp_ID',)
    search_fields = ('bp_ID',)


class BloodGlucoseMonitorAdmin(ImportExportModelAdmin):
    exclude = ('created_at',)
    fields = ()
    readonly_fields = ()
    sortable_by = 'id'
    date_hierarchy = 'created_at'
    list_display = ('blood_glucose_ID',)

    search_fields = ('blood_glucose_ID',)

class WeighScaleAdmin(ImportExportModelAdmin):
    exclude = ('created_at',)
    fields = ()
    readonly_fields = ()
    sortable_by = 'id'
    date_hierarchy = 'created_at'
    list_display = ('weigh_scale_ID',)

    search_fields = ('weigh_scale_ID',)


class PatientDeviceInformationAdmin(ImportExportModelAdmin):

    # fieldsets = [
    #     ('PatientID', {'fields': ['firstName', 'lastName','gender','phoneNumber','DOB','address','medicareNumber',]}),
    #     ('BpMonitorID', {'fields': ['bpID']}),
    #     ('MedicalBranch', {'fields': ['branchName']}),
    #     ('BloodGlucoseMonitor', {'fields': ['bloodGlucoseID']}),
    #     ('Oxymeter', {'fields': ['pulseOxymeterID']}),
    #     ('WeighScale', {'fields': ['WeighScaleID']}),
    #     ('Tablet', {'fields': ['tabletSerialID','tabletImei','simNumber',]}),
    #     ('Survey', {'fields': ['firstSurveyDate','surveyStatus','startofVHS','VHSFamily',]}),
    # ]

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
    list_display = ('patient_ID','bp_monitor_ID','blood_glucose_monitor','oxymeter_ID','medical_branch_ID','tablet_ID','survey_ID','weigh_scale_ID','created_by')

    search_fields = [
        'patient_ID__name', 'patient_ID__lastName','patient_ID__gender',
                     'patient_ID__phone_number','patient_ID__DOB','patient_ID__address',
                     'patient_ID__medicare_number','medical_branch_ID__branch_name','bp_monitor_ID__bp_ID',
                     'blood_glucose_monitor__blood_glucose_ID','oxymeter_ID__pulse_oxymeter_ID',
                     'tablet_ID__tablet_serial_ID','tablet_ID__tablet_imei','tablet_ID__sim_umber',
                     'survey_ID__first_survey_date','survey_ID__survey_status','survey_ID__start_of_VHS',
                     'survey_ID__VHS_family','weigh_scale_ID__weigh_scale_ID'
    ]


admin.site.register(Patient,PatientAdmin)
admin.site.register(Survey,SurveyAdmin)
admin.site.register(MedicalBranch,MedicalBranchAdmin)
admin.site.register(Tablet,TabletAdmin)
admin.site.register(Oxymeter,OxymeterAdmin)
admin.site.register(BpMonitor,BpMonitorAdmin)
admin.site.register(BloodGlucoseMonitor,BloodGlucoseMonitorAdmin)
admin.site.register(WeighScale,WeighScaleAdmin)
admin.site.register(PatientDeviceInformation,PatientDeviceInformationAdmin)


