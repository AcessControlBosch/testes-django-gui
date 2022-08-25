from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from rest_framework.permissions import IsAuthenticated

class UserAPI(APIView):

    def get(self, request, pk=""):

        if 'name' in request.GET:
            currentlyName = request.GET['name']
            users = User.objects.filter(name__contains=currentlyName)
            serializer = UserTable(users, many=True)
            return Response(serializer.data)

        elif 'user' in request.GET:
            currentlyUser = request.GET['user']
            users = Users.objects.filter(idUser=currentlyUser)
            serializer = UserTable(users, many=True)
            return Response(serializer.data)

        elif pk == '':
            users = User.objects.all()
            serializer = UserTable(users, many=True)
            return Response(serializer.data)

        else:
            users = User.objects.get(id=pk)
            serializer = UserTable(users)
            return Response(serializer.data)

    def post(self, request):

        serializer = UserTable(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})

    def put(self, request, pk=''):

        users = User.objects.get(id=pk)
        serializer = UserTable(users, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):    

        users = User.objects.get(id=pk)       
        users.delete()
        return Response({"msg": "Apagado com sucesso"})

class ApprenticeAPI(APIView):

    def get(self, request, pk=''):

        if 'name' in request.GET:
            currentlyName = request.GET['name']
            apprentice = Apprentice.objects.filter(name__contains=currentlyName)
            serializer = ApprenticeTable(apprentice, many=True)
            return Response(serializer.data)

        elif 'pk' in request.GET:
            currentlyID = request.GET['pk']
            apprentice = Apprentice.objects.filter(name__contains=currentlyID)
            serializer = ApprenticeTable(apprentice, many=True)
            return Response(serializer.data)
        
        elif pk == '':
            apprentice = Apprentice.objects.all()
            serializer = ApprenticeTable(apprentice, many=True)
            return Response(serializer.data)

        else:
            apprentice = User.objects.get(id=pk)
            serializer = ApprenticeTable(apprentice)
            return Response(serializer.data)
            

    def post(self, request):

        serializer = ApprenticeTable(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})

    def put(self, request, pk=''):

        apprentices = Apprentice.objects.get(id=pk)
        serializer = ApprenticeTable(apprentices, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):

        apreentice = Apprentice.objects.get(id=pk)       
        apreentice.delete()
        return Response({"msg": "Apagado com sucesso"})

class typeAssocienteAPI(APIView):

    def get(self, request, pk=""):

        if pk == '':
            typeAssocienteResult = typeAssociente.objects.all()
            serializer = typeAssocienteTable(typeAssocienteResult, many=True)
            return Response(serializer.data)

        else:
            typeAssocienteResult = User.objects.get(id=pk)
            serializer = typeAssocienteTable(typeAssocienteResult)
            return Response(serializer.data)
    
    def post(self, request):

        serializer = typeAssocienteTable(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})

    def put(self, request, pk=""):

        typeAssocienteResults = typeAssociente.objects.get(id=pk)
        serializer = typeAssocienteTable(typeAssocienteResults, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk=""):

        typeAssocienteResults = typeAssociente.objects.get(id=pk)       
        typeAssocienteResults.delete()
        return Response({"msg": "Apagado com sucesso"})

class AssociateAPI(APIView):

    def get(self, request, pk=''):

        if pk == '':
            associateResult = Associate.objects.all()
            serializer = AssociateTable(associateResult, many=True)
            return Response(serializer.data)

        else:
            associateResult = Associate.objects.get(id=pk)
            serializer = AssociateTable(associateResult)
            return Response(serializer.data)

    def post(self, request):

        serializer = AssociateTable(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})
    
    def put(self, request, pk=''):

        AssocienteResults = Associate.objects.get(id=pk)
        serializer = AssociateTable(AssocienteResults, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk=''):

        AssocienteResults = Associate.objects.get(id=pk)       
        AssocienteResults.delete()
        return Response({"msg": "Apagado com sucesso"})


class MachineAPI(APIView):

    def get(self, request, pk=''):

        if pk == '':
            machineResult = Machine.objects.all()
            serializer = MachineTable(machineResult, many=True)
            return Response(serializer.data)

        else:
            machineResult = Machine.objects.get(id=pk)
            serializer = MachineTable(machineResult)
            return Response(serializer.data)

    def post(self, request):

        serializer = MachineTable(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})
    
    def put(self, request, pk=''):

        machineResult = Machine.objects.get(id=pk)
        serializer = MachineTable(machineResult, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk=''):

        machineResult = Machine.objects.get(id=pk)       
        machineResult.delete()
        return Response({"msg": "Apagado com sucesso"})

class QuestionAPI(APIView):

    def get(self, request, pk=''):

        if pk == '':
            questionResult = Question.objects.all()
            serializer = QuestionTable(questionResult, many=True)
            return Response(serializer.data)

        else:
            questionResult = Question.objects.get(id=pk)
            serializer = QuestionTable(questionResult)
            return Response(serializer.data)

    def post(self, request):

        serializer = QuestionTable(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})
    
    def put(self, request, pk=''):

        questionResult = Question.objects.get(id=pk)
        serializer = QuestionTable(questionResult, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk=''):

        questionResult = Question.objects.get(id=pk)       
        questionResult.delete()
        return Response({"msg": "Apagado com sucesso"})

class CourseAPI(APIView):

    def get(self, request, pk=''):

        if pk == '':
            courseResult = Courses.objects.all()
            serializer = CoursesTable(courseResult, many=True)
            return Response(serializer.data)

        else:
            courseResult = Courses.objects.get(id=pk)
            serializer = CoursesTable(courseResult)
            return Response(serializer.data)

    def post(self, request):

        serializer = CoursesTable(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})
    
    def put(self, request, pk=''):

        courseResult = Courses.objects.get(id=pk)
        serializer = CoursesTable(courseResult, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk=''):

        courseResult = Courses.objects.get(id=pk)       
        courseResult.delete()
        return Response({"msg": "Apagado com sucesso"})

class GreenBookAPI(APIView):

    def get(self, request, pk='', tq=''):

        if pk == '':
            greenBookResult = GreenBook.objects.all()
            serializer = GreenBookTable(greenBookResult, many=True)
            return Response(serializer.data)

        else:
            greenBookResult = GreenBook.objects.filter(idMachineFK=pk, typeQuestion=tq)
            serializer = GreenBookTable(greenBookResult, many=True)
            return Response(serializer.data)
            

    def post(self, request):

        serializer = GreenBookTable(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})
    
    def put(self, request, pk=''):

        greenBookResult = GreenBook.objects.get(id=pk)
        serializer = GreenBookTable(greenBookResult, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk=''):

        greenBookResult = GreenBook.objects.get(id=pk)       
        greenBookResult.delete()
        return Response({"msg": "Apagado com sucesso"})

class MaintenanceAPI(APIView):

    def get(self, request, pk=''):

        if pk == '':
            maintenanceResult = Maintenance.objects.all()
            serializer = MaintenanceTable(maintenanceResult, many=True)
            return Response(serializer.data)

        else:
            maintenanceResult = Maintenance.objects.get(id=pk)
            serializer = MaintenanceTable(maintenanceResult)
            return Response(serializer.data)

    def post(self, request):

        serializer = MaintenanceTable(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})
    
    def put(self, request, pk=''):

        maintenanceResult = Maintenance.objects.get(id=pk)
        serializer = MaintenanceTable(maintenanceResult, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk=''):

        maintenanceResult = Maintenance.objects.get(id=pk)       
        maintenanceResult.delete()
        return Response({"msg": "Apagado com sucesso"})

class ReleaseMachineAPI(APIView):

    def get(self, request, pk=''):

        if pk == '':
            releaseMachineTableResult = ReleaseMachine.objects.all()
            serializer = ReleaseMachineTable(releaseMachineTableResult, many=True)
            return Response(serializer.data)

        else:
            releaseMachineTableResult = ReleaseMachine.objects.get(id=pk)
            serializer = ReleaseMachineTable(releaseMachineTableResult)
            return Response(serializer.data)

    def post(self, request):

        serializer = ReleaseMachineTable(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})
    
    def put(self, request, pk=''):

        releaseMachineTableResult = ReleaseMachine.objects.get(id=pk)
        serializer = ReleaseMachineTable(releaseMachineTableResult, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk=''):

        releaseMachineTableResult = ReleaseMachine.objects.get(id=pk)       
        releaseMachineTableResult.delete()
        return Response({"msg": "Apagado com sucesso"})


class QRcodeAPI(APIView):

    def get(self, request, pk=''):

        if pk == '':
            QRcodeTableResult = QRcode.objects.all()
            serializer = QRcodeTable(QRcodeTableResult, many=True)
            return Response(serializer.data)

        else:
            QRcodeTableResult = QRcode.objects.get(id=pk)
            serializer = QRcodeTable(QRcodeTableResult)
            return Response(serializer.data)

    def post(self, request):

        serializer = QRcodeTable(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})
    
    def put(self, request, pk=''):

        QRcodeTableResult = QRcode.objects.get(id=pk)
        serializer = QRcodeTable(QRcodeTableResult, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk=''):

        QRcodeTableResult = QRcode.objects.get(id=pk)       
        QRcodeTableResult.delete()
        return Response({"msg": "Apagado com sucesso"})


class ObservationAPI(APIView):

    def get(self, request, pk=''):

        if pk == '':
            ObservationResult = Observation.objects.all()
            serializer = ObservationTable(ObservationResult, many=True)
            return Response(serializer.data)

        else:
            ObservationResult = Observation.objects.get(id=pk)
            serializer = ObservationTable(ObservationResult)
            return Response(serializer.data)

    def post(self, request):

        serializer = ObservationTable(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})
    
    def put(self, request, pk=''):

        ObservationResult = Observation.objects.get(id=pk)
        serializer = ObservationTable(ObservationResult, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk=''):

        ObservationResult = Observation.objects.get(id=pk)       
        ObservationResult.delete()
        return Response({"msg": "Apagado com sucesso"})

class MaintenanceOrderAPI(APIView):

    def get(self, request, pk=''):

        if pk == '':
            MaintenanceOrderTableResult = MaintenanceOrder.objects.all()
            serializer = MaintenanceOrderTable(MaintenanceOrderTableResult, many=True)
            return Response(serializer.data)

        else:
            MaintenanceOrderTableResult = MaintenanceOrder.objects.get(id=pk)
            serializer = MaintenanceOrderTable(MaintenanceOrderTableResult)
            return Response(serializer.data)


    def post(self, request):

        serializer = MaintenanceOrderTable(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})
    
    def put(self, request, pk=''):

        MaintenanceOrderTableResult = MaintenanceOrder.objects.get(id=pk)
        serializer = MaintenanceOrderTable(MaintenanceOrderTableResult, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk=''):

        MaintenanceOrderTableResult = MaintenanceOrder.objects.get(id=pk)       
        MaintenanceOrderTableResult.delete()
        return Response({"msg": "Apagado com sucesso"})


class AreaAPI(APIView):

    def get(self, request, pk=''):

        if pk == '':
            AreaResult = Areas.objects.all()
            serializer = AreasTable(AreaResult, many=True)
            return Response(serializer.data)

        else:
            AreaResult = Areas.objects.get(id=pk)
            serializer = AreasTable(AreaResult)
            return Response(serializer.data)


    def post(self, request):

        serializer = AreasTable(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})
    
    def put(self, request, pk=''):

        AreaResult = Areas.objects.get(id=pk)
        serializer = AreasTable(AreaResult, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk=''):

        AreaResult = Areas.objects.get(id=pk)       
        AreaResult.delete()
        return Response({"msg": "Apagado com sucesso"})

class RequestLoginAPI(APIView):

    def get(self, request, pk=''):

        if pk == '':
            RequestLoginResult = RequestLogin.objects.all()
            serializer = RequestLoginTable(RequestLoginResult, many=True)
            return Response(serializer.data)

        else:
            RequestLoginResult = RequestLogin.objects.get(id=pk)
            serializer = RequestLoginTable(RequestLoginResult)
            return Response(serializer.data)


    def post(self, request):

        serializer = RequestLoginTable(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})
    
    def put(self, request, pk=''):

        RequestLoginResult = RequestLogin.objects.get(id=pk)
        serializer = RequestLoginTable(RequestLoginResult, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk=''):

        RequestLoginResult = RequestLogin.objects.get(id=pk)       
        RequestLoginResult.delete()
        return Response({"msg": "Apagado com sucesso"})