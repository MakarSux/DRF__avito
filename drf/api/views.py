from django.forms.models import model_to_dict
from django.shortcuts import render

from rest_framework import generics

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


from rest_framework import viewsets
 