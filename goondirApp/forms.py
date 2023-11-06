from django import forms
from .models import *


# creating a patient form
class PatientForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Patient

        # specify fields to be used
        fields = '__all__'

class SurveyForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Survey

        # specify fields to be used
        fields = '__all__'

class OxymeterForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model =Oxymeter

        # specify fields to be used
        fields = '__all__'

class bpmonitorForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = BpMonitor

        # specify fields to be used
        fields = '__all__'

class BloodGlucoseMonitorForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = BloodGlucoseMonitor

        # specify fields to be used
        fields = '__all__'

class WeighScaleForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = WeighScale

        # specify fields to be used
        fields = '__all__'

class surveyForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Survey

        # specify fields to be used
        fields = '__all__'

class TabletForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Tablet

        # specify fields to be used
        fields = '__all__'

class MedicalBranchForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = MedicalBranch

        # specify fields to be used
        fields = '__all__'

class PatientDeviceInformationForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = PatientDeviceInformation

        # specify fields to be used
        fields = '__all__'

class surveyForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Survey

        # specify fields to be used
        fields = '__all__'
