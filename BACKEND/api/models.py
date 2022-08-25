from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

#impede a criação de usuários com emails repetidos
#User._meta.get_field('email')._unique = True
#impede com que o email seja null ou vazio durante cadastro
#User._meta.get_field('email').blank = False
#User._meta.get_field('email').null = False

class User(models.Model):

    # permission_classes = (IsAuthenticated,)

    name = models.CharField(max_length=100)
    EDV = models.CharField(max_length=10)
    id_card = models.CharField(max_length=30, null=True, blank= True, default=0)

    def __str__(self):
        return self.name

class Courses(models.Model):

    # permission_classes = (IsAuthenticated,)

    name=models.CharField(max_length=25)
    
    def __str__(self):
        return self.name

class Apprentice(models.Model):

    # permission_classes = (IsAuthenticated,)

    course = models.ForeignKey(Courses, related_name="courseApprentice", on_delete=models.CASCADE)
    idApprenticeFK = models.ForeignKey(User, related_name="userApprentice", on_delete=models.CASCADE)

class typeAssociente(models.Model):

    # permission_classes = (IsAuthenticated,)

    type = models.CharField(max_length=30)

    def __str__(self):
        return self.type

class Associate(models.Model):

    # permission_classes = (IsAuthenticated,)

    type = models.ForeignKey(typeAssociente, related_name="typeAssociente", on_delete=models.CASCADE)
    idAssociateFK = models.ForeignKey(User, related_name="userADM", on_delete=models.CASCADE)

class Machine(models.Model):

    # permission_classes = (IsAuthenticated,)

    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    status = models.BooleanField()
    ipaddress = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Question(models.Model):

    # permission_classes = (IsAuthenticated,)

    type = models.CharField(max_length=15)

    def __str__(self):
        return self.type

class Areas(models.Model):

    # permission_classes = (IsAuthenticated,)

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class GreenBook(models.Model):

    # permission_classes = (IsAuthenticated,)

    idMachineFK = models.ForeignKey(Machine, related_name="machineGreenBook", on_delete=models.CASCADE)
    typeQuestion = models.ForeignKey(Question, related_name="question", on_delete=models.CASCADE)
    question = models.CharField(max_length=50)

class Maintenance(models.Model):

    # permission_classes = (IsAuthenticated,)

    date = models.DateField()
    hour = models.TimeField()
    idMachineFK = models.ForeignKey(Machine, related_name="machineMaintenance", on_delete=models.CASCADE)
    idAssociateFK = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)

class ReleaseMachine(models.Model): 

    # permission_classes = (IsAuthenticated,)

    date = models.DateField()
    hourInitial = models.TimeField()
    hourFinish = models.TimeField(default=True)
    idMachineFK = models.ForeignKey(Machine, related_name="machineReleaseMachine", on_delete=models.CASCADE)
    idAssociateFK = models.ForeignKey(User, related_name="userReleaseMachine", on_delete=models.CASCADE)

class QRcode(models.Model):

    # permission_classes = (IsAuthenticated,)

    router_ip = models.CharField(max_length=300)
    idMachineFK = models.ForeignKey(Machine, related_name="machineQRcode", on_delete=models.CASCADE)

class Observation(models.Model):

    # permission_classes = (IsAuthenticated,)

    date = models.DateField()
    hour = models.TimeField()
    idMachineFK = models.ForeignKey(Machine, related_name="machineObservation", on_delete=models.CASCADE)
    idAssociateFK = models.ForeignKey(User, related_name="userObservation", on_delete=models.CASCADE)

class MaintenanceOrder(models.Model):

    # permission_classes = (IsAuthenticated,)

    status = models.CharField(max_length=15)
    idMachineFK = models.ForeignKey(Machine, related_name="machineMaintenanceOrder", on_delete=models.CASCADE)
    idAssociateFK = models.ForeignKey(User, related_name="userMaintenanceOrder", on_delete=models.CASCADE)

class RequestLogin(models.Model):

    name = models.CharField(max_length=200)
    EDV = models.CharField(max_length=15)
    idAreaFK = models.ForeignKey(Areas, related_name="areas", on_delete=models.CASCADE)