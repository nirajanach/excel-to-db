"""goondirProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views

admin.autodiscover()
urlpatterns = [

    path('dashboard', views.dashboard, name='dashboard'),

    path('upload/', views.upload_xls, name='upload'),
    # path('patients/',views.getPatients),
    # path('logout/', views.logout)

    path('patients/list', views.patients_list, name='patients_list'),
    path('patient/create', views.patient_create, name='patient_create'),
    path('patient/edit/<int:pk>', views.patient_edit, name="patient_edit"),
    path('patient/delete/<int:pk>', views.patient_delete, name="patient_delete"),
    path('patient/profile/<int:pk>', views.patient_profile, name='patient_profile'),

    path('survey/list', views.survey_list, name='survey_list'),
    path('survey/create', views.survey_create, name='survey_create'),
    path('survey/edit/<int:pk>', views.survey_edit, name="survey_edit"),
    path('survey/delete/<int:pk>', views.survey_delete, name="survey_delete"),

    path('oxymeter/list', views.oxymeter_list, name='oxymeter_list'),
    path('oxymeter/create', views.oxymeter_create, name='oxymeter_create'),
    path('oxymeter/edit/<int:pk>', views.oxymeter_edit, name="oxymeter_edit"),
    path('oxymeter/delete/<int:pk>', views.oxymeter_delete, name="oxymeter_delete"),

    path('bpmonitor/list', views.bpmonitor_list, name='bpmonitor_list'),
    path('bpmonitor/create', views.bpmonitor_create, name='bpmonitor_create'),
    path('bpmonitor/edit/<int:pk>', views.bpmonitor_edit, name="bpmonitor_edit"),
    path('bpmonitor/delete/<int:pk>', views.bpmonitor_delete, name="bpmonitor_delete"),

    path('bloodglucosemonitor/list', views.bloodglucosemonitor_list, name='bloodglucosemonitor_list'),
    path('bloodglucosemonitor/create', views.bloodglucosemonitor_create, name='bloodglucosemonitor_create'),
    path('bloodglucosemonitor/edit/<int:pk>', views.bloodglucosemonitor_edit, name="bloodglucosemonitor_edit"),
    path('bloodglucosemonitor/delete/<int:pk>', views.bloodglucosemonitor_delete, name="bloodglucosemonitor_delete"),
    
    path('weighscale/list', views.weighscale_list, name='weighscale_list'),
    path('weighscale/create', views.weighscale_create, name='weighscale_create'),
    path('weighscale/edit/<int:pk>', views.weighscale_edit, name="weighscale_edit"),
    path('weighscale/delete/<int:pk>', views.weighscale_delete, name="weighscale_delete"),

    path('tablet/list', views.tablet_list, name='tablet_list'),
    path('tablet/create', views.tablet_create, name='tablet_create'),
    path('tablet/edit/<int:pk>', views.tablet_edit, name="tablet_edit"),
    path('tablet/delete/<int:pk>', views.tablet_delete, name="tablet_delete"),
    
    path('medicalbranch/list', views.medicalbranch_list, name='medicalbranch_list'),
    path('medicalbranch/create', views.medicalbranch_create, name='medicalbranch_create'),
    path('medicalbranch/edit/<int:pk>', views.medicalbranch_edit, name="medicalbranch_edit"),
    path('medicalbranch/delete/<int:pk>', views.medicalbranch_delete, name="medicalbranch_delete"),

    # path('patientdeviceinformation/list', views.patientdeviceinformation_list, name='patientdeviceinformation_list'),
    # path('patientdeviceinformation/create', views.patientdeviceinformation_create, name='patientdeviceinformation_create'),
    # path('patientdeviceinformation/edit/<int:pk>', views.patientdeviceinformation_edit, name="patientdeviceinformation_edit"),
    # path('patientdeviceinformation/delete/<int:pk>', views.patientdeviceinformation_delete, name="patientdeviceinformation_delete"),
    
    

]
