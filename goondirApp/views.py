from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, permission_required
from tablib import Dataset
from .resources import *
from .models import *
from .forms import *
from django.db import transaction, IntegrityError
from django.contrib import messages


# Create your views here.


def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


@login_required
# @permission_required('goondirApp.')
def upload_xls(request):
    if request.method == 'POST':
        patient_information_resource = PatientDeviceInformationResource()
        patient_resource = PatientResource()
        dataset = Dataset()
        input_file = request.FILES['myfile']

        imported_data = dataset.load(input_file.read(), format='xlsx')
        # print(imported_data)
        for data in imported_data:
            print(data[2])
            patient_model = Patient(
                name=data[3],
                gender=data[4],
                DOB=data[7],
                medicare_number=data[8],
                address=data[14],

            )
            oxymeter_model=Oxymeter(
            pulse_oxymeter_ID=data[16]
            )
            survey_model = Survey(
                first_survey_date=data[12],
                survey_status=data[10],
                start_of_VHS=data[11],
                VHS_family='dsa'
            )

            bpMonitor_model = BpMonitor(
                bp_ID=data[17]
            )

            bloodGlucose_model = BloodGlucoseMonitor(
                blood_glucose_ID=data[18]
            )

            weighScale_model = WeighScale(
                weigh_scale_ID=data[19]
            )

            tablet_model = Tablet(
                tablet_serial_ID=data[20],
                tablet_imei=data[21],
                sim_number=data[15]
            )

            medicalBranch_model = MedicalBranch(
                branch_name=data[6]
                # branchLocation_model=data[]

            )

            # print(patient_model.firstName, patient_model.gender, patient_model.phoneNumber, patient_model.address)
            patient_model.save()
            oxymeter_model.save()
            survey_model.save()
            bpMonitor_model.save()
            bloodGlucose_model.save()
            medicalBranch_model.save()
            weighScale_model.save()
            tablet_model.save()
            patient_model_id = Patient.objects.latest('id')
            oxymeter_model_id = Oxymeter.objects.latest('id')
            survey_model_id = Survey.objects.latest('id')
            bpMonitor_model_id = BpMonitor.objects.latest('id')
            bloodGlucose_model_id = BloodGlucoseMonitor.objects.latest('id')
            medical_branch_model_id = MedicalBranch.objects.latest('id')
            weigh_scale_model_id = WeighScale.objects.latest('id')
            tablet_model_id = Tablet.objects.latest('id')
            patient_device_information_model=PatientDeviceInformation(
                patient_ID=patient_model_id,
                bp_monitor_ID=bpMonitor_model_id,
                blood_glucose_monitor=bloodGlucose_model_id,
                oxymeter_ID=oxymeter_model_id,
                weigh_scale_ID=weigh_scale_model_id,
                medical_branch_ID=medical_branch_model_id,
                tablet_ID=tablet_model_id,
                survey_ID=survey_model_id,
                
                )
            patient_device_information_model.save()
            
        return render(request, '../templates/goondirApp/upload/upload.html')

    else:
        return render(request, '../templates/goondirApp/upload/upload.html')

@login_required
def dashboard(request):
    # total_patient = {"patients": Patient.objects.all().count}
    total_patient_count=Patient.objects.all().count()
    total_tablet_count=Patient.objects.all().count()
    context = {"total_patient_count":total_patient_count,
    "total_tablet_count":total_tablet_count}
    return render(request, "../templates/goondirApp/dashboard.html", context)


# Patients
@login_required
def patients_list(request):
    context = {"patients": Patient.objects.all()}
    return render(request, "../templates/goondirApp/patient/list.html", context)


def patient_create(request):
    context = {}
    form = PatientForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('patients_list')
    
    context['form'] = form
    context['model']='Patient'
    return render(request, "../templates/goondirApp/partials/form.html", context)

def patient_edit(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    form = PatientForm(request.POST or None, instance=patient)
    if form.is_valid():
        form.save()
        return redirect('patients_list')
    context = {"form": form}
    context['model']='Patient'
    return render(request, "../templates/goondirApp/partials/form.html", context)


def patient_delete(request, pk):
    obj = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('patients_list')
    context = {"patient": obj}
    return render(request, "../templates/goondirApp/patient/delete.html", context)

    
# Survey
def survey_list(request):
    context = {"survey": Survey.objects.all()}
    return render(request, "../templates/goondirApp/survey/list.html", context)


def survey_create(request):
    context = {}
    form = surveyForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('surveys_list')

    context['form'] = form
    context['model']='Survey'
    return render(request, "../templates/goondirApp/survey/create.html", context)

def survey_edit(request, pk):
    survey = get_object_or_404(Survey, pk=pk)
    form = surveyForm(request.POST or None, instance=survey)
    if form.is_valid():
        form.save()
        return redirect('surveys_list')
    context = {"form": form}
    context['model']='Survey'
    return render(request, "../templates/goondirApp/survey/edit.html", context)


def survey_delete(request, pk):
    obj = get_object_or_404(Survey, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('surveys_list')
    context = {"survey": obj}
    return render(request, "../templates/goondirApp/survey/delete.html", context)

    # oxymeter
def oxymeter_list(request):
    context = {"oxymeters": Oxymeter.objects.all()}
    return render(request, "../templates/goondirApp/oxymeter/list.html", context)


def oxymeter_create(request):
    context = {}
    form = OxymeterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('oxymeters_list')

    context['form'] = form
    return render(request, "../templates/goondirApp/oxymeter/create.html", context)

def oxymeter_edit(request, pk):
    oxymeter = get_object_or_404(Oxymeter, pk=pk)
    form = OxymeterForm(request.POST or None, instance=oxymeter)
    if form.is_valid():
        form.save()
        return redirect('oxymeters_list')
    context = {"form": form}
    context['model']='Patient'
    return render(request, "../templates/goondirApp/oxymeter/edit.html", context)


def oxymeter_delete(request, pk):
    obj = get_object_or_404(Oxymeter, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('oxymeters_list')
    context = {"oxymeter": obj}
    return render(request, "../templates/goondirApp/oxymeter/delete.html", context)

    # bpmonitor
def bpmonitor_list(request):
    context = {"bpmonitors": BpMonitor.objects.all()}
    return render(request, "../templates/goondirApp/bpmonitor/list.html", context)


def bpmonitor_create(request):
    context = {}
    form = BpMonitorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('bpmonitors_list')

    context['form'] = form
    return render(request, "../templates/goondirApp/bpmonitor/create.html", context)

def bpmonitor_edit(request, pk):
    bpmonitor = get_object_or_404(BpMonitor, pk=pk)
    form = bpmonitorForm(request.POST or None, instance=bpmonitor)
    if form.is_valid():
        form.save()
        return redirect('bpmonitors_list')
    context = {"form": form}
    context['model']='Patient'
    return render(request, "../templates/goondirApp/bpmonitor/edit.html", context)


def bpmonitor_delete(request, pk):
    obj = get_object_or_404(BpMonitor, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('bpmonitors_list')
    context = {"bpmonitor": obj}
    return render(request, "../templates/goondirApp/bpmonitor/delete.html", context)
  # bloodglucosemonitor
def bloodglucosemonitor_list(request):
    context = {"bloodglucosemonitors": BloodGlucoseMonitor.objects.all()}
    return render(request, "../templates/goondirApp/bloodglucosemonitor/list.html", context)


def bloodglucosemonitor_create(request):
    context = {}
    form = BloodGlucoseMonitorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('bloodglucosemonitors_list')

    context['form'] = form
    return render(request, "../templates/goondirApp/bloodglucosemonitor/create.html", context)

def bloodglucosemonitor_edit(request, pk):
    bloodglucosemonitor = get_object_or_404(BloodGlucoseMonitor, pk=pk)
    form = BloodGlucoseMonitorForm(request.POST or None, instance=bloodglucosemonitor)
    if form.is_valid():
        form.save()
        return redirect('bloodglucosemonitors_list')
    context = {"form": form}
    context['model']='Patient'
    return render(request, "../templates/goondirApp/bloodglucosemonitor/edit.html", context)


def bloodglucosemonitor_delete(request, pk):
    obj = get_object_or_404(BloodGlucoseMonitor, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('bloodglucosemonitors_list')
    context = {"bloodglucosemonitor": obj}
    return render(request, "../templates/goondirApp/bloodglucosemonitor/delete.html", context)

     # weighscale
def weighscale_list(request):
    context = {"weighscales": WeighScale.objects.all()}
    return render(request, "../templates/goondirApp/weighscale/list.html", context)


def weighscale_create(request):
    context = {}
    form = WeighScaleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('weighscales_list')

    context['form'] = form
    return render(request, "../templates/goondirApp/weighscale/create.html", context)

def weighscale_edit(request, pk):
    weighscale = get_object_or_404(WeighScale, pk=pk)
    form = WeighScaleForm(request.POST or None, instance=weighscale)
    if form.is_valid():
        form.save()
        return redirect('weighscales_list')
    context = {"form": form}
    context['model']='Patient'
    return render(request, "../templates/goondirApp/weighscale/edit.html", context)


def weighscale_delete(request, pk):
    obj = get_object_or_404(WeighScale, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('weighscales_list')
    context = {"weighscale": obj}
    return render(request, "../templates/goondirApp/weighscale/delete.html", context)

     # tablet
def tablet_list(request):
    context = {"tablets": Tablet.objects.all()}
    return render(request, "../templates/goondirApp/tablet/list.html", context)


def tablet_create(request):
    context = {}
    form = TabletForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('tablets_list')

    context['form'] = form
    return render(request, "../templates/goondirApp/tablet/create.html", context)

def tablet_edit(request, pk):
    tablet = get_object_or_404(Tablet, pk=pk)
    form = TabletForm(request.POST or None, instance=tablet)
    if form.is_valid():
        form.save()
        return redirect('tablets_list')
    context = {"form": form}
    context['model']='Patient'
    return render(request, "../templates/goondirApp/tablet/edit.html", context)


def tablet_delete(request, pk):
    obj = get_object_or_404(Tablet, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('tablets_list')
    context = {"tablet": obj}
    return render(request, "../templates/goondirApp/tablet/delete.html", context)

     # medicalbranch
def medicalbranch_list(request):
    context = {"medicalbranchs": MedicalBranch.objects.all()}
    return render(request, "../templates/goondirApp/medicalbranch/list.html", context)


def medicalbranch_create(request):
    context = {}
    form = MedicalBranchForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('medicalbranchs_list')

    context['form'] = form
    return render(request, "../templates/goondirApp/medicalbranch/create.html", context)

def medicalbranch_edit(request, pk):
    medicalbranch = get_object_or_404(MedicalBranch, pk=pk)
    form = MedicalBranchForm(request.POST or None, instance=medicalbranch)
    if form.is_valid():
        form.save()
        return redirect('medicalbranchs_list')
    context = {"form": form}
    context['model']='Patient'
    return render(request, "../templates/goondirApp/medicalbranch/edit.html", context)


def medicalbranch_delete(request, pk):
    obj = get_object_or_404(MedicalBranch, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('medicalbranchs_list')
    context = {"medicalbranch": obj}
    return render(request, "../templates/goondirApp/medicalbranch/delete.html", context)



def patient_profile(request):
    return render(request, '../templates/goondirApp/account/profile.html')