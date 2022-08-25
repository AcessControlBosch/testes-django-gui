from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path("users/", UserAPI.as_view(), name="users"),
    path("users/<int:pk>/", UserAPI.as_view(), name="usersParameters"),

    path("apprentices/", ApprenticeAPI.as_view(), name="apprentices"),
    path("apprentices/<int:pk>/", UserAPI.as_view(), name="apprenticesParameters"),

    path("typeAssociente/", typeAssocienteAPI.as_view(), name="typeAssocientes"),
    path("typeAssociente/<int:pk>/", typeAssocienteAPI.as_view(), name="typeAssocientesParameters"),

    path("associates/", AssociateAPI.as_view(), name="associates"),
    path("associates/<int:pk>/", AssociateAPI.as_view(), name="associatesParameters"),

    path("machines/", MachineAPI.as_view(), name="machines"),
    path("machines/<int:pk>/", MachineAPI.as_view(), name="machinesParameters"),

    path("questions/", QuestionAPI.as_view(), name="questions"),
    path("questions/<int:pk>/", QuestionAPI.as_view(), name="questionsParameters"),

    path("courses/", CourseAPI.as_view(), name="courses"),
    path("courses/<int:pk>/", CourseAPI.as_view(), name="coursesParameters"),

    path("greenbooks/", GreenBookAPI.as_view(), name="greenbooks"),
    path("greenbooks/<int:pk>/<int:tq>/", GreenBookAPI.as_view(), name="greenbooksParameters"),

    path("maintenances/", MaintenanceAPI.as_view(), name="maintenances"),
    path("maintenances/<int:pk>/", MaintenanceAPI.as_view(), name="maintenancesParameters"),

    path("releasemachines/", ReleaseMachineAPI.as_view(), name="releasemachines"),
    path("releasemachines/<int:pk>/", ReleaseMachineAPI.as_view(), name="releasemachinesParameters"),

    path("qrcodes/", QRcodeAPI.as_view(), name="qrcodes"),
    path("qrcodes/<int:pk>/", QRcodeAPI.as_view(), name="qrcodesParameters"),

    path("observations/", ObservationAPI.as_view(), name="observations"),
    path("observations/<int:pk>/", ObservationAPI.as_view(), name="observationsParameters"),

    path("maintenanceorders/", MaintenanceOrderAPI.as_view(), name="maintenanceorders"),
    path("maintenanceorders/<int:pk>/", MaintenanceOrderAPI.as_view(), name="maintenanceordersParameters"),

    path("areas/", AreaAPI.as_view(), name="areas"),
    path("areas/<int:pk>/", AreaAPI.as_view(), name="areasParameters"),

    path("requestLogins/", RequestLoginAPI.as_view(), name="requestLogins"),
    path("requestLogins/<int:pk>/", RequestLoginAPI.as_view(), name="requestLoginsParameters"),

]