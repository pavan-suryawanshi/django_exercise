from django.shortcuts import render
from django.http import JsonResponse
from firstApp.models import Employee
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def employeeView(request):
    emp = {
    'id':123,
    'name':'Pavan',
    'sal': 100000
    }

    data = Employee.objects.all();
    response = {'employees':list(data.values('name','sal'))}

    return JsonResponse(response)

    permission_classes = (IsAuthenticated,)
