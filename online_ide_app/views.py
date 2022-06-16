from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from .utils import *

# Create your views here.
def hello_world(request):
    return HttpResponse("Welcome to online ide")

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SubmissionsViewSet(ModelViewSet):
    queryset = Submissions.objects.all()
    serializer_class = SubmissionSerializer

    def create(self, request, *args, **kwargs):
        request.data["status"]="P"
        file_name=create_code_file(request.data.get("code"),request.data.get("language"))
        output=execute_code_file(file_name,request.data.get("language"))
        request.data["output"]=output
        return super().create(request,args,kwargs)
