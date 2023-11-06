from import_export import resources
from .models import *

class PatientDeviceInformationResource(resources.ModelResource):
    class Meta:
        model = PatientDeviceInformation

class PatientResource(resources.ModelResource):
    class Meta:
        model =Patient

class SurveyResource(resources.ModelResource):
    class Meta:
        model =Survey

class OxymeterResource(resources.ModelResource):
    class Meta:
        model =Oxymeter

class BpMonitorResource(resources.ModelResource):
    class Meta:
        model =BpMonitor

class WeighScaleResource(resources.ModelResource):
    class Meta:
        model =WeighScale

class MedicalBranchResource(resources.ModelResource):
    class Meta:
        model =MedicalBranch


